from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import ProductForm
from .models import Product, Category
from .services import get_products_by_category


class ProductListView(ListView):
    """Список товаров — доступен всем."""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    """Страница контактов — доступна всем."""
    template_name = 'catalog/contacts.html'


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    """Детали товара — кешируются на 15 минут."""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CategoryProductsView(DetailView):
    """Список продуктов в категории — использует сервис с кешем."""
    model = Category
    template_name = 'catalog/category_products.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем продукты через сервисную функцию
        context['products'] = get_products_by_category(self.object.pk)
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание товара — только для авторизованных."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирование товара — только для владельца или модератора."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.has_perm('catalog.can_unpublish_product')


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление товара — только для владельца или модератора."""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.has_perm('catalog.delete_product')

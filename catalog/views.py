from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    """Список товаров — доступен всем."""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    """Страница контактов — доступна всем."""
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    """Детали товара — доступны всем."""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание товара — только для авторизованных."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование товара — только для авторизованных."""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление товара — только для авторизованных."""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')

from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})

from django.urls import path

from .views import (
    ContactsView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    CategoryProductsView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', CategoryProductsView.as_view(), name='category_products'),
]

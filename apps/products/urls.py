from django.urls import path

from .views import (
	ProductCreateView,
	ProductDetailView,
	ProductUpdateView,
	ProductDeleteView,
	UserProductsView
)

from . signals import ProductManage


urlpatterns = [
	path('create', 
		ProductCreateView.as_view(), name='product-create'),
	path('product/detail/<int:product_id>', 
		ProductDetailView, name='product-detail'),
	path('product/update/<int:product_id>', 
		ProductUpdateView.as_view(), name='product-update'),
	path('product/delete/<int:product_id>', 
		ProductDeleteView, name='product-delete'),
	path('user-products/<int:user_id>', 
		UserProductsView, name='user-products'),
]
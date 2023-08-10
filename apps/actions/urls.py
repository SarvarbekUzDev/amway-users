from django.urls import path

from .views import (
	UserProductsView
)


urlpatterns = [
	path('user-products/<int:user_id>/<int:worker_id>',
		UserProductsView, name='user-products')
]
from django.urls import path

from .views import (
	UserCreateView,
	UserDetailView,
	UserUpdateView,
)

from .signals import SendTokenEmail


urlpatterns = [
	path('register', 
		UserCreateView.as_view(), name='user-register'),
	path('user/detail/<int:user_id>', 
		UserDetailView, name='user-detail'),
	path('user/update/<int:user_id>', 
		UserUpdateView.as_view(), name='user-update'),
]
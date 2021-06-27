from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('admin/', views.admin, name='admin/'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('exit', views.exit, name='exit')
]
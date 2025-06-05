from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
    path('check/', views.check, name='check'),
]
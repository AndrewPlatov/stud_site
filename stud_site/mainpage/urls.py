from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main),
    path('test1/', views.test1, name='test1'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html')),
]
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
    path('check/', views.check, name='check'),
    path('student_cabinet/', views.student_cabinet, name='student_cabinet'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('homework/upload/', views.homework_upload, name='homework_upload'),
    path('homework/download/', views.homework_download, name='homework_download'),
]
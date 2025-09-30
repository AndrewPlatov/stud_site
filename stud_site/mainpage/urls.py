from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_user, name='register'),
    path('teacher/register/', views.register_teacher, name='teacher_register'),
    path('teacher/profile/', views.teacher_profile, name='teacher_profile'),
    path('teacher/login/', views.teacher_login, name='teacher_login'),
    path('take_test/', views.take_test, name='take_test'),
    path('create_test/', views.create_test, name='create_test'),
    path('test_list/', views.test_list, name='test_list'),
    path('merge_test/', views.merge_test, name='merge_test'), 
    path('test/<int:test_id>/take/', views.take_test, name='take_test'),
    path('test/<int:test_id>/delete/', views.delete_test, name='delete_test'),
    path('edit_test/', views.edit_test, name='edit_test'),
    path('test/result/', views.test_result, name='test_result'),
    path('question/<int:pk>/edit/', views.question_edit, name='question_edit'),
    path('question/<int:pk>/delete/', views.question_delete, name='question_delete'),
    path('question/create/', views.question_create, name='question_create'),
    path('student/tests/', views.student_test_list, name='student_test_list'),
    # path('teacher/profile/edit/', views.edit_teacher_profile, name='edit_teacher_profile'),
    path('check/', views.check, name='check'),
    path('student_cabinet/', views.student_cabinet, name='student_cabinet'),
    # path('update_profile/', views.update_profile, name='update_profile'),
    path('homework/upload/', views.homework_upload, name='homework_upload'),
    path('homework/download/', views.homework_download, name='homework_download'),
]
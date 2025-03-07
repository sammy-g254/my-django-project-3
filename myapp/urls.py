from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views

urlpatterns = [
    path('', views.student_list, name='index'),
    path('create/', views.create_student, name='create'),
    #path('<int:pk>/', views.student_detail, name='detail'),
    #path('<int:pk>/update/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
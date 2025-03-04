from django.urls import path

from .import views

urlpatterns = [
    path('', views.student_list, name='index'),
    path('create/', views.create_student, name='create'),
    #path('<int:pk>/', views.student_detail, name='detail'),
    #path('<int:pk>/update/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('register/', views.register_user, name='register')
]
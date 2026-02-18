from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<str:register_no>/', views.view_result, name='view_result'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-subject/<int:student_id>/', views.add_subject, name='add_subject_for_student'),
    path('students/', views.student_list, name='student_list'),
    path('edit-subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
]

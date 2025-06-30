# Miprimerapagina/pag/urls.py (cambia 'Miprimerapagina/pag' por el nombre real de tu aplicación si es diferente)
from django.urls import path
from .views import (
    course_list_view, course_detail_view, course_create,
    course_edit, course_delete_view,
)


  
      
app_name = 'pag' # <--- ¡AÑADE ESTA LÍNEA!

urlpatterns = [
    # URLs para Cursos
    path('courses/', course_list_view, name='course_list'),
    path('courses/<int:pk>/', course_detail_view, name='course_detail'),
    path('courses/create/', course_create, name='course_create'),
    path('courses/<int:pk>/edit/', course_edit, name='course_edit'),
    path('courses/<int:pk>/delete/', course_delete_view, name='course_delete'),
]
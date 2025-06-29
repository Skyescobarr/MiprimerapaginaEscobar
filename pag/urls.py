# Miprimerapagina/pag/urls.py (cambia 'Miprimerapagina/pag' por el nombre real de tu aplicación si es diferente)
from django.urls import path
# Importa directamente las clases de vista desde tu archivo views.py
from .views import (
    course_list_view,
    course_detail_view,
    course_create_view,
    course_update_view,
    course_delete_view, 
)

  
      
urlpatterns = [
    # Rutas para el modelo Course
    # Cuando usas una clase de vista, siempre llamas a .as_view()
    path('courses/', course_list_view, name='course_list'),
    path('courses/<int:pk>/', course_detail_view, name='course_detail'),
    path('courses/create/', course_create_view, name='course_create'),
    path('courses/<int:pk>/update/', course_update_view, name='course_update'),
    path('courses/<int:pk>/delete/', course_delete_view, name='course_delete'),
    
]
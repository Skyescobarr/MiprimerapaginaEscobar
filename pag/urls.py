# Miprimerapagina/pag/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.new_post, name='new_post'),
    path('category/new/', views.new_category, name='new_category'),
    path('search/', views.post_search, name='post_search'),
]
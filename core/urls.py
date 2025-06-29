from django.urls import path
from .views import HomeView, AboutView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'), # Ruta principal de core, será la de inicio
    path('about/', AboutView.as_view(), name='about'),  # Ruta para la página 'Acerca de'
]
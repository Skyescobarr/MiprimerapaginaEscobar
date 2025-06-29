from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Formulario de creación de usuarios de Django
from django.contrib import messages # Para mostrar mensajes al usuario

class HomeView(TemplateView):
    """
    Vista para la página de inicio.
    """
    template_name = 'core/home.html'

class AboutView(TemplateView):
    """
    Vista para la página 'Acerca de'.
    """
    template_name = 'core/about.html'

def register(request):
    """
    Vista para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login') # Redirige a la página de login después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

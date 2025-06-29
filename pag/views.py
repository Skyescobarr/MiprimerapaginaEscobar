# tu_app_nombre/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Si aún usas UserCreationForm para registrar usuarios:
from django.contrib.auth.forms import UserCreationForm


# ¡Importa tus modelos y formularios actualizados!
from .models import Course, Instructor # Asegúrate de que estos son los nombres de tus modelos
from .forms import CourseForm, CourseSearchForm # Importa solo los formularios que usarás


# --- Vistas Generales ---
def home_view(request):
    """
    Vista para la página de inicio.
    Renderiza el template home.html.
    """
    return render(request, 'home.html') # Asegúrate de que 'home.html' está en la carpeta 'templates' de tu app o proyecto

def about_view(request):
    return render(request, 'about.html') , {'titulo': 'Acerca de Nosotros'}



def contact_view(request):
    """
    Vista para la página de contacto.
    (Aquí podrías añadir lógica para un formulario de contacto si lo deseas).
    """
    return render(request, 'contact.html')

# --- Vistas de Cursos ---
def course_list_view(request): # Renombrado de post_list_view
    """
    Vista para listar todos los cursos y permitir búsquedas.
    """
    courses = Course.objects.all().order_by('-published_date') # Obtiene todos los cursos ordenados

    search_form = CourseSearchForm(request.GET) # Instancia el formulario de búsqueda con los datos de GET
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            # Filtra los cursos cuyo título contenga la 'query' (insensible a mayúsculas/minúsculas)
            courses = courses.filter(title__icontains=query)

    return render(request, 'course_list.html', {
        'courses': courses,
        'search_form': search_form
    })

@login_required # Solo usuarios autenticados pueden crear cursos
def course_create_view(request): # Renombrado de post_create_view
    """
    Vista para crear un nuevo curso.
    """
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            # El campo 'instructor' se maneja directamente por el formulario ModelForm.
            # No necesitas asignar el 'author' si tu modelo Course no tiene ese campo.
            form.save()
            messages.success(request, '¡Curso creado con éxito!')
            return redirect('course_list') # Redirige a la lista de cursos
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form}) # Usar un template más genérico para formularios

def course_detail_view(request, pk):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

# --- Vistas de Autenticación (si son personalizadas) ---
def register_view(request):
    """
    Vista para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def course_update_view(request, pk):
    """
    Vista para actualizar un curso existente.
    """
    course = get_object_or_404(Course, pk=pk)

    # Opcional: Asegúrate de que solo el instructor del curso (o staff/superusuario) puede editar
    # if not is_instructor_or_staff(request.user) and request.user != course.instructor.user:
    #     messages.error(request, 'No tienes permiso para editar este curso.')
    #     return redirect('course_detail', pk=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course) # Pasa la instancia del curso
        if form.is_valid():
            form.save()
            messages.success(request, '¡Curso actualizado con éxito!')
            return redirect('course_detail', pk=course.pk) # Redirige al detalle del curso
    else:
        form = CourseForm(instance=course) # Pasa la instancia para pre-llenar el formulario
    return render(request, 'course_form.html', {'form': form, 'course': course})
def course_delete_view(request, pk):
    """
    Vista para eliminar un curso existente.
    """
    course = get_object_or_404(Course, pk=pk)

    # Opcional: Asegúrate de que solo el instructor del curso (o staff/superusuario) puede eliminar
    # if not is_instructor_or_staff(request.user) and request.user != course.instructor.user:
    #     messages.error(request, 'No tienes permiso para eliminar este curso.')
    #     return redirect('course_detail', pk=pk)

    if request.method == 'POST':
        course.delete()
        messages.success(request, '¡Curso eliminado con éxito!')
        return redirect('course_list') # Redirige a la lista de cursos después de eliminar
    return render(request, 'course_confirm_delete.html', {'course': course}) # Pide confirmación al usuario

# Si tienes Category y Comment, y sus vistas asociadas, deberías renombrarlas también
# def category_list_view(request): # Eliminar si no tienes modelo Category
#     # ...
# def comment_create_view(request, pk): # Eliminar si no tienes modelo Comment
#     # ...

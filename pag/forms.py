
# tu_app_nombre/forms.py

from django import forms
# ¡Importa los modelos correctos que están definidos en tu models.py!
from .models import Course, Instructor # Ahora importamos Course e Instructor

# ====================================================================
# Formulario para crear o editar un Curso (anteriormente PostForm)
# ====================================================================
class CourseForm(forms.ModelForm): # Renombrado de PostForm a CourseForm
    """
    Formulario para crear o actualizar instancias del modelo Course.
    """
    class Meta:
        model = Course # Ahora apunta a tu modelo Course
        # Los campos deben coincidir con los de tu modelo Course
        fields = ['title', 'description', 'instructor', 'published_date', 'students_count']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Descripción detallada del curso...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Título del curso'}),
            'published_date': forms.DateInput(attrs={'type': 'date'}), # Widget para fecha
            # Si instructor es un ForeignKey a un modelo con muchos objetos, Django renderizará un <select>
        }
        labels = {
            'title': 'Título del Curso',
            'description': 'Descripción del Curso',
            'instructor': 'Instructor del Curso',
            'published_date': 'Fecha de Publicación',
            'students_count': 'Número de Estudiantes',
        }
        # Si quieres que 'students_count' se gestione automáticamente y no sea editable por el usuario:
        # exclude = ['students_count']
        # Si 'published_date' se asigna automáticamente en el `save` del modelo y no quieres que el usuario lo establezca:
        # exclude = ['published_date']


# ====================================================================
# Formulario para crear o editar un Instructor (opcional, si lo necesitas en el front-end)
# ====================================================================
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre completo del instructor'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico único'}),
        }
        labels = {
            'name': 'Nombre del Instructor',
            'email': 'Email del Instructor',
        }


# ====================================================================
# Formulario de Búsqueda de Cursos (anteriormente PostSearchForm)
# ====================================================================
class CourseSearchForm(forms.Form): # Renombrado de PostSearchForm a CourseSearchForm
    """
    Formulario básico para la búsqueda de Cursos por título.
    """
    query = forms.CharField(
        label='Buscar Curso por Título',
        max_length=100,
        required=False, # Que no sea un campo obligatorio para la búsqueda
        widget=forms.TextInput(attrs={'placeholder': 'Buscar cursos por título...'})
    )


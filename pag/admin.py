from django.contrib import admin
from .models import Course, Instructor # Importa ambos modelos

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'published_date', 'students_count')
    list_filter = ('published_date', 'instructor')
    search_fields = ('title', 'description')
    date_hierarchy = 'published_date'
    # Asegúrate de que 'instructor' esté en los campos del formulario si no usas '__all__'
    fields = ('title', 'description', 'instructor', 'published_date', 'students_count')

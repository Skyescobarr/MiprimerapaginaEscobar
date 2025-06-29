from django.db import models
from django.utils import timezone # Para usar timezone.now

class Instructor(models.Model):
    """
    Modelo para representar a los instructores de los cursos.
    Campos:
        name (CharField): Nombre del instructor.
        email (EmailField): Correo electrónico del instructor (debe ser único).
    """
    name = models.CharField(max_length=100, verbose_name="Nombre del Instructor")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"
        ordering = ['name'] # Ordenar por nombre por defecto

    def __str__(self):
        return self.name

class Course(models.Model):
    """
    Modelo para representar los cursos.
    Campos:
        title (CharField): Título del curso.
        description (TextField): Descripción del curso.
        students_count (IntegerField): Contador de estudiantes inscritos en el curso.
        published_date (DateField): Fecha de publicación del curso (opcional).
        instructor (ForeignKey): Relación con el modelo Instructor.
    """
    title = models.CharField(max_length=200, verbose_name="Título del Curso")
    description = models.TextField(verbose_name="Descripción")
    students_count = models.IntegerField(default=0, verbose_name="Número de Estudiantes")
    published_date = models.DateField(blank=True, null=True, verbose_name="Fecha de Publicación")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses', verbose_name="Instructor")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-published_date', 'title'] # Ordenar por fecha descendente y luego por título

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para asignar la fecha de publicación
        si no se ha establecido y el curso es nuevo.
        """
        if not self.published_date and not self.pk: # Si es un nuevo curso y no tiene fecha
            self.published_date = timezone.now().date() # Asigna la fecha actual
        super().save(*args, **kwargs)

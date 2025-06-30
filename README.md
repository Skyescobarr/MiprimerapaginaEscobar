# Mi Blog Django (MiPrimeraPaginaEscobar)

Este proyecto es una aplicación web construida con Django que simula un sistema de gestión de blog. Permite a los usuarios registrarse, iniciar sesión, y a los administradores realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las publicaciones.

## Requisitos del Sistema
* Python 3.11
* Django 5.2.3 

## Configuración y Ejecución Local

1.  **Clonar el repositorio:**
    ```bash
    git clone  https://github.com/Skyescobarr/MiprimerapaginaEscobar.git
    cd Miprimerapagina # O el nombre de tu carpeta
    ```

2.  **Crear y activar el entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows PowerShell:
    .\venv\Scripts\Activate.ps1
    # En Linux/macOS o Git Bash:
    # source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install Django 
    ```

4.  **Aplicar migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario (para acceder al panel de administración):**
    ```bash
    python manage.py createsuperuser
    ```
    User: Sky
    Pass: --------

6.  **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    Accede a la aplicación en `http://127.0.0.1:8000/`.

## Funcionalidades Principales


### Funcionalidades de Cursos

* **Listado de Cursos:** `http://127.0.0.1:8000/course/list/`
* **Crear Nuevo Curso:** `http://127.0.0.1:8000/course/create/`
* **Eliminar Curso:** `http://127.0.0.1:8000/course/delete/<id>/`
* **Formulario de Curso:** `http://127.0.0.1:8000/course/form/`
* **Cursos Disponibles:** `http://127.0.0.1:8000/courses/`
* **Ver Curso :** `http://127.0.0.1:8000/course/<id>/`
* **Editar Curso:** `http://127.0.0.1:8000/course/edit/<id>/`
* **Panel de Administración:** `http://127.0.0.1:8000/admin/` (usa el superusuario creado).

* `Miprimerapagina/`: Carpeta principal del proyecto Django.
* `pag/`: Aplicación principal del blog (contiene modelos, vistas, formularios, etc.).
* `templates/`: Contiene `base.html` y una subcarpeta `pag/` con las plantillas de la aplicación.
* `db.sqlite3`: Base de datos SQLite (ignorada por Git).
* `venv/`: Entorno virtual de Python (ignorado por Git).

## Dos aplicaciones
* core: Maneja las páginas principales como el inicio y "Acerca de"
* blog: Gestiona modelos de Post y Author y sus respectivas vistas CRUD 

## Modelos 
* **Post:** Posee campos de texto (título, contenido), numérico (contador de vistas) y fechas (fecha de publicación)
* **Author:** Posee campos de texto

## Vistas Basadas en Clases (CBV) 
* CourseListView para listar publicaciones 
* CourseDetailView para ver el detalle de la publicación
* CourseListView para crear nuevos cursos
* CourseDeleteView para eliminar publicaciones
 
## Autenticación de usuarios
* Registro de nuevos usuarios
* Inicio de sesión de usuarios existentes

## Funcionalidad de Administrador
* Los usuarios superadministradores (`is_superuser` o `is_staff`) pueden realizar operaciones CRUD en las publicaciones a través del panel de admin y las vistas frontend.

admin  
user: skyescobarr  
pass: Alix7413

## Navegación Intuitiva 
* Redirección de la ruta base (/) a la página de inicio (/home/)
* Navegación entre las diferentes secciones de la aplicación utilizando enlaces en la interfaz de usuario, sin necesidad de manipular la barra de direcciones.

---

Desarrollado por Skylix Escobar

## Cambios Realizados
- Se separaron las aplicaciones en `core` (páginas principales) y `pag` (gestión de cursos e instructores).
- Se implementaron modelos personalizados para `Instructor` y `Course` (curso).
- Se agregaron vistas basadas en clases (CBV) para listar, crear, ver detalle y eliminar cursos.
- Se habilitó el registro y autenticación de usuarios.
- Se configuró el panel de administración para gestión avanzada de cursos y usuarios.
- Se mejoró la navegación con enlaces y redirección automática de la ruta base.
- Se agregaron formularios personalizados para la creación y edición de cursos y categorías.
- Se protegieron las vistas sensibles mediante permisos y autenticación.
- Se documentó la estructura del proyecto y los comandos principales en este README.

---

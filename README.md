# Mi Blog Django (TuPrimeraPagina+Apellido)

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
    pip install Django # O pip install -r requirements.txt si creaste uno
    ```
    (Si no tienes un `requirements.txt`, sería buena idea crearlo con `pip freeze > requirements.txt` y subirlo al repo).

4.  **Aplicar migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario (para acceder al panel de administración):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear usuario y contraseña.

6.  **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    Accede a la aplicación en `http://127.0.0.1:8000/`.

## Funcionalidades Principales

* **Listado de Posts:** `http://127.0.0.1:8000/`
* **Detalle de Post:** Haz clic en un post en la lista.
* **Crear Nuevo Post:** `http://127.0.0.1:8000/post/new/` (o haz clic en "Nuevo Post" en la navegación).
* **Crear Nueva Categoría:** `http://127.0.0.1:8000/category/new/` (o haz clic en "Nueva Categoría" en la navegación).
* **Buscar Posts:** `http://127.0.0.1:8000/search/` (o haz clic en "Buscar Post" en la navegación).
* **Panel de Administración:** `http://127.0.0.1:8000/admin/` (usa el superusuario creado).

## Estructura del Proyecto

* `Miprimerapagina/`: Carpeta principal del proyecto Django.
* `pag/`: Aplicación principal del blog (contiene modelos, vistas, formularios, etc.).
* `templates/`: Contiene `base.html` y una subcarpeta `pag/` con las plantillas de la aplicación.
* `db.sqlite3`: Base de datos SQLite (ignorada por Git).
* `venv/`: Entorno virtual de Python (ignorado por Git).

## Dos aplicaciones
* core: Maneja las páginas principales como el inicio y "Acerca de"
* blog: Gestiona modelos de Post y Author y sus respectivas vistas CRUD 

## Modelos 
*Post: Posee campos de texto(título, contenido), númerico(contador de vistas) y fechas (fecha de publicación)
*Author: Posee campos de texto

# Vistas Basadas en Clases(CBV) 
* ListasView para listar publicaciones 
* DetailView para ver el detalle de la publicacion
* CreateView para crear nuevas publicaciones
* DeleteView para eliminar publicaciones

# Autenticación de usuarios
*Registro de nuevos usuarios
*Inicio de sesión de usuarios existentes

# Funcionalidad de Administrador: 
* Los usuarios superadministradores (is_superuser o is_staff)pueden realizar operaciones CRUD en las publicaciones a través del panel de admin y las vistas frontend

# Navegación Intuitiva 
* Redirección de la ruta base (/) a la página de inicio (/home/)
* Navegación entre las diferentes secciones de la aplicación utilizando enlaces en la interfaz de usuario, sin necesidad de manipular la barra de direcciones.

---
Desarrollado por Skylix Escobar
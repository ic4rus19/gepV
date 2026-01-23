Python 3.12.8

Borrado de memoria de PS:
    %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt   Donde encontrarlo
    C:\Users\rojos\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

*******************************************CREAMOS ENTORNO VIRTUAL*********************************
*******************************************especificamente para cualquier proyecto*********************************
1. mkdir nProyecto          Creamos la carpeta con el nombre el proyecto
2. cd .\nProyecto\          Accedemos
3. python -m venv nProyecto Creamos el entorno del proyecto para agregar las dependencias
4.  .\env\Scripts\activate  ACTIVAMOS ------------------IMPORTANTE-----------------
5. pip list                 Muestra lo que tenemos instalado para el proyecto
6. python.exe -m pip install --upgrade pip     ---------Por si no esta actualizado.
7. pip install flask        Instalamos flask
8. pip llist                Comprobamos
9. deactivate               Desactivamos el entorno

INSTALACIÓN DE DEPENDENCIAS PARA LOS PROYECTOS
11.Formularios o Editor de texto enriquecido en tus formularios Flask
    pip install -U Flask-WTF
    pip install flask-ckeditor
12.flask SQLAlchemy         Base de Datos
    pip install Flask-SQLAlchemy

          
         
*******************************************especificamente para cualquier proyecto*********************************
13. Se creara la carpeta instance con la bd creada y le cambiaremos el nombre 
    esto establecera la conexión con exito......Leccion 36

👉GET: Pedir datos.
  Se usa para mostrar páginas o formularios.
  No modifica nada.

👉POST: Enviar datos.
  Se usa para guardar, crear o modificar información.
  Envía datos de forma segura (no en la URL).


ATENTOS A LA CLASE 11..

# Utilizar el entorno de pruebas de phytonAnywhere

# Creamos en nuestro proyecto el archivo de requirements.txt
    pip freeze > requirements.txt
# Creamos el repositorio github (fáci)
# Desde nuestro PC directorio de nuestros proyectos.
    con powershell:
    git clone https://github.com/ic4rus19/portafolio.git
# Se generamos la carpeta y copiamos todo de una a otra.
Desde la nueva carpeta accedemos a code . 

Luego vamos a Pythoanywhere
    El dominio sera de pruebas y cogeara el nombre de:
         ic4rus.pythonanywhere.com. 

Qué es realmente un “env”
Un venv es una carpeta con:
    un Python “aislado” (o enlaces),pip, y todas las librerías que instalas (Flask, etc.)
Sirve para que tu proyecto use sus propias dependencias y versiones, sin mezclarlas con otros proyectos del sistema.

# ---ATENCIÓN-----
# Desde la consola en el servidor, creamos el entorno virtual.
- Podemos mirar la documentación:
    https://help.pythonanywhere.com/pages/Flask/
    Desde la raiz en bash del servidor:
        python --version
        git --version
        mkvirtualenv --python=python3.13 .env-list
        clonamos nuestro repositorio
        git clone https://github.com/ic4rus19/list-todo.git
        instalamos los requerimientos de la aplicación
        pip install -r requirements.txt
        pip list
    Desplegamos desde el servidor
        Eliminamos la antrior proyecto
        Creamos una nueva pero con configuración manual.
        Coloacamos la ruta del proyecto---pwd---
        Colocamos la ruta del env creado en el servidor
            which python
            /home/ic4rus/.virtualenvs/.env-list
        Por ultimo modificamos el archivo xxxxwsgi.py
        
        
        import sys
            # Añadimos la carpeta raíz del proyecto al path de Python
            # para que el servidor pueda encontrar nuestros módulos
            # (run.py, dashboard, etc.)
                    project_home = '/home/ic4rus/list-todo'
                    if project_home not in sys.path:
                        sys.path = [project_home] + sys.path

            # Importamos la aplicación Flask desde run.py
            # La renombramos como "application" porque los servidores WSGI
            # esperan que la app se llame exactamente así
                    from run import app as application  # noqa

        Hacemos reload y comprobamos el funcionamiento


Endpoint =  El identificador interno de una ruta que apunta a una función.
            Flask enruta por endpoints, no por archivos
            url_for() siempre usa endpoints
            Con Blueprints: blueprint.funcion

*************************************PROYECTO SPACIOS PUBLICOS**************************************
Craación, lectura y buscador de blogs. (ESPACIOS PUBLICOS)
    Editar el blog y trabajar con el texto.
    Buscador de blogs, que tengan que ver con la busqueda realizada.
    Tambien crearemos un registro. Nombre y correo.
    Tendremos un apartado para crear o modificar nuestros blogs.
        Modificaciones de perfil.
            Nombre o usuario o cambiar contraseña.
        Añadir blog.
            Trabajar con un editor de texto e importador de img.
        Ver las publicaciones.

1.- Creamos carpeta nProyecto:         mkdir nProyecto
2.- Creamos entorno virtual:           python -m venv nProyecto
3.- Activamos entorno:                 .\env-blog\Scripts\activate
4.- Instalamos Flask y actualizamos:   pip install flask
5.- Con el entorno activado instalaremos las dependencia de python
    

INICIAR APLICACIÓN: PYTHON RUN.PY
    mabel@gmail   1234 -------Tenemos el apartado de cambiar contraseña

**5.- Creamos archivos o estructura:**
        1. Principal arranque aplicación: run.py
        2. Donde estara la configuración: config.py
        3. Directorio principal:
            blogr
                4.-  __init_.py. Se usa para iniciar la app.
                5.- templates. Carpeta para las plantillas.
                6.- statics. Para los estaticos.
                7.- auth.py . Para la autentificación. Vistas y rutas.
                8.- post.py . Para las publicaciones.
                9.- home.py . Para la páguina principal.
                10- models.py . Creacion de modelos                
        **ESTRUCTURA BASE DEL PROYECTO**
                
            
6.- Creamos las vistas o Blue Print. Desde home.py

7.- Instalacion de https://www.postgresql.org/
    Video de instalación:  https://www.youtube.com/watch?v=n5Ec9bMouWQ
    Librerias que utilizaremos para la conexión de la bd
        pip install flask-sqlalchemy
        pip install psycopg2
        pip list

    Como hacer la configuración:
        https://flask-sqlalchemy.readthedocs.io/en/stable/config/#configuration-keys
        # PostgreSQL
        postgresql://scott:tiger@localhost/project


Endpoint =  El identificador interno de una ruta que apunta a una función.
            Flask enruta por endpoints, no por archivos
            url_for() siempre usa endpoints
            Con Blueprints: blueprint.funcion

# Actualizaciones de GitHub desde PC
        git add .
        git commit -m "gepv02"
        git push origin main  

# Desde Servidor(enconsola y desde el directorio de la app)
    git pull

# Comprovaciones:
    cd ~/gepVallgorguina
    git log -1 --oneline




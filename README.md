Python 3.12.8


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

# INSTALACIÓN DE DEPENDENCIAS PARA LOS PROYECTOS
11. Formularios o Editor de texto enriquecido en tus formularios Flask
    pip install -U Flask-WTF
    pip install flask-ckeditor
12. flask SQLAlchemy         Base de Datos
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


# ENTORNO DE PRUEBAS de phytonAnywhere

# 1- Creamos en nuestro proyecto el archivo de requirements.txt
        pip freeze > requirements.txt
# 2- Creamos el repositorio github (fáci)
        Nuevo repositorio etc.
# 3- Git en nuestro PC directorio de nuestros proyectos.
        git log --oneline (Historial de commits).
        git add .
        git commit -m "Organiza..."
        git push


# Pythoanywhere
    El dominio sera de pruebas y cogeara el nombre del correo:
        ic4rus.pythonanywhere.com.
         Accedemos a pythoanywhere      

# Desde pythonAnywhere ---- WEB CREAMOS Add a new web app
    Nos dara a elegir el framework:
        Flask:
            Selecionamos la Versión.
            Creara la aplicación y nos mnostrara la ruta.
            Inspecionamos des de web:
                Apartado Code
                    Atentos wsgi.py donde estará la configuración.
                Revisamos todas las pestañas y nos hacemos con el menu:
                    Podemos acceder a la consola que sera de LINUX.
                Virtualenv:
                Qué es realmente un “env”???????
                        Un venv es una carpeta con un Python “aislado” (o enlaces),pip, y todas las librerías que instalas (Flask, etc.)
                        Sirve para que tu proyecto use sus propias dependencias y versiones, sin mezclarlas con otros proyectos del sistema.
                Creamos el entorno virtual: (IMPORTANTISIMO)
                # ---ATENCIÓN-----
                # Desde la consola en el servidor, CREAMOS el entorno virtual y clonamos el PROYECTO
                - Podemos mirar la documentación:
                    https://help.pythonanywhere.com/pages/Flask/
                    Desde la raiz en bash del servidor:
                        python --version
                        git --version
                        mkvirtualenv --python=python3.13 .Nombre del entornoVirtual
                    Clonamos nuestro repositorio
                        git clone https://github.com/ic4rus19/list-todo.git
                    Instalamos los requerimientos de la aplicación
                        pip install -r requirements.txt
                        pip list      
# DESPLEGAR LA APLICACIÓN
    Borramos la anterior:
    Add a new web app
        Manual configuration:
            En WEB:
            Coloacamos la ruta del proyecto
                pwd
            Colocamos la ruta del env creado en el servidor
                which python
                    /home/ic4rus/.virtualenvs/.env-list
            ***************Por ultimo modificamos el archivo xxxxwsgi.py

                import sys
                project_home = '/home/ic4rus/Nom.PROYECTO'
                if project_home not in sys.path:
                    sys.path = [project_home] + sys.path
                from run import app as application  # noqa

            Reload desde WEB

# Actualizaciones de GitHub desde PC
        git add .
        git commit -m "gepv02"
        git push

# Desde Servidor(enconsola y desde el directorio env)
    Por primera vez:
        git clone https://github.com/ic4rus19/gepVallgorguina.git
    Luego:    
        git pull

# Comprovaciones:
    cd ~/gepVallgorguina
    git log -1 --oneline

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


# Endpoint =  El identificador interno de una ruta que apunta a una función.
    Flask enruta por endpoints, no por archivos
    url_for() siempre usa endpoints
    Con Blueprints: blueprint.funcion






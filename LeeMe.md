Funcion para mos trar nuestro tree:
    function Show-Tree {
    param([string]$Path = ".", [int]$Depth = 2, [int]$CurrentLevel = 0)
    if ($CurrentLevel -gt $Depth) { return }
    $indent = "  " * $CurrentLevel
    Get-ChildItem -Path $Path -Directory | ForEach-Object {
        Write-Output "$indent+-- $($_.Name)"
        Show-Tree -Path $_.FullName -Depth $Depth -CurrentLevel ($CurrentLevel + 1)
    }
}
# Ejecutar desde el directorio actual, mostrando hasta 2 niveles
Show-Tree -Depth 2   


Recursos:
    Bootstrap
    FonsoneW


GIT:
1) 🖥️ Primera vez en tu PC (Windows)
    1. Clonar el repo (recomendado por SSH)
    git clone git@github.com:ic4rus19/gepV.git
    cd gepV

2. Crear entorno virtual
    python -m venv .venv

3. Activar entorno
    .\.venv\Scripts\Activate.ps1

4. Instalar dependencias
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

5. Arrancar Flask (forma segura)
    python -m flask --app app --debug run

2) 🔁 Flujo normal en tu PC (cambios/modificaciones)
    A) Si has cambiado código / html / css (lo típico)
    git status
    git add .
    git commit -m "mensaje claro"
    git push

B) Si además has instalado librerías nuevas
Instalas:

    python -m pip install NOMBRE_LIBRERIA
    Actualizas requirements.txt:

    python -m pip freeze > requirements.txt
    Subes cambios:
        git add requirements.txt
        git commit -m "Update requirements"
        git push

3) 🌍 Primera vez en PythonAnywhere
    1. Clonar el repo (SSH)
        git clone git@github.com:ic4rus19/gepV.git
        cd gepV

    2. Crear venv (ejemplo con Python 3.12)
        mkvirtualenv envVallgorguina --python=python3.12
        workon envVallgorguina

    3. Instalar dependencias
        pip install --upgrade pip
        pip install -r requirements.txt

    4. Configurar Web (una sola vez)
    En PythonAnywhere:

        Web → Add a new web app
        Manual configuration → Python 3.12
        En Virtualenv pon:
        /home/ic4rus/.virtualenvs/envVallgorguina

        Luego en el WSGI file (Web → WSGI configuration):

        apunta tu app a app.py (si quieres, me pegas tu WSGI y te lo dejo perfecto)

        4) 🔁 Flujo normal en PythonAnywhere (actualizaciones/modificaciones)
            A) Si solo has cambiado código (lo normal)
            cd ~/gepV
            workon envVallgorguina
            git pull
            Web → Reload

            B) Si también cambiaste requirements.txt
            cd ~/gepV
            workon envVallgorguina
            git pull
            pip install -r requirements.txt
            Web → Reload
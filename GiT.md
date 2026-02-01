# Guía Git – Proyecto GEPV

Esta guía describe **el flujo correcto de trabajo con Git** para el proyecto **GEPV**, 
desde la creación del repositorio en GitHub hasta el trabajo diario entre **PC (desarrollo)** y **PythonAnywhere (producción)**.

---

## 0️⃣ Paso previo (una sola vez en GitHub)

Antes de todo:

* Crear el repositorio en GitHub (`gepV`)
* Puede estar vacío o con README inicial
* Público o privado (indistinto)

> GitHub actúa como **almacén central del código**.

---

## 1️⃣ Primera vez en tu PC (desarrollo)

### 1. Clonar el repositorio (recomendado por SSH)

```bash
git clone git@github.com:ic4rus19/gepV.git
cd gepV
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Arrancar el proyecto Flask

```bash
python -m flask --app app --debug run
```
### 6. Que dependencia tengo
  ```bash
 pip freeze > requirements.txt
---

## 2️⃣ Flujo normal en tu PC (modificaciones)

### A) Cambios normales (código, HTML, CSS)

```bash
git status
git add .
git commit -m "mensaje claro del cambio"
git push
```

### B) Si añades nuevas librerías

```bash
pip install nombre_libreria
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push
```

---

## 3️⃣ Primera vez en PythonAnywhere

### 1. Clonar el repositorio

```bash
git clone git@github.com:ic4rus19/gepV.git
cd gepV
```

### 2. Crear entorno virtual

```bash
mkvirtualenv envVallgorguina --python=python3.12
workon envVallgorguina
```

### 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar Web App (una sola vez)

* Web → Add a new web app
* Manual configuration
* Python 3.12
* Virtualenv: `/home/ic4rus/.virtualenvs/envVallgorguina`
* WSGI apuntando a `app.py`

---

## 4️⃣ Flujo normal en PythonAnywhere (actualizaciones)

### A) Cambios normales

```bash
cd ~/gepV
workon envVallgorguina
git pull
```

Luego:

* Web → Reload

### B) Si cambió `requirements.txt`

```bash
cd ~/gepV
workon envVallgorguina
git pull
pip install -r requirements.txt
```

Luego:

* Web → Reload

---

## ⚠️ Caso especial: rebase / force push

Si se ha reescrito el historial en GitHub:

```bash
git fetch origin
git reset --hard origin/main
```

---

## 🧠 Reglas de oro

* El entorno virtual **NO se sube a Git** (`.venv`, `env*` en `.gitignore`)
* `requirements.txt` es la referencia de dependencias
* En servidores, **usar siempre SSH**
* El código se edita **solo en el PC**, no en PythonAnywhere

---

## 📌 Resumen mental

* **GitHub** → almacén
* **PC** → desarrollo
* **PythonAnywhere** → despliegue

---

Fin de la guía.

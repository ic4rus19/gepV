
# !ARANQUE DE LA APLICACIÓN
# !flask --app app --debug run


from flask import Flask, Blueprint, render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

from sqlalchemy import func



app = Flask(__name__)

# DB en instance/ (recomendado en Flask)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gep.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------- MODELO ----------
class NetejaSetmanal(db.Model):
    __tablename__ = "neteja_setmanal"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=True)
    torn = db.Column(db.String(20), nullable=True)
    dia = db.Column(db.Date, nullable=True)
    centre = db.Column(db.String(255), nullable=True)
    inici = db.Column(db.String(10), nullable=True)
    fi = db.Column(db.String(10), nullable=True)
    temps = db.Column(db.String(10), nullable=True)


# ---------- RUTAS EXISTENTES ----------
@app.route("/")
def index():
    return render_template("index.html")


# ---------- /NETEJA ----------
def parse_date_q(q):
    """Intenta convertir el texto de búsqueda en una fecha."""
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d/%m"):
        try:
            d = datetime.strptime(q, fmt)
            # si no hay año, asumimos el actual
            if "%Y" not in fmt:
                d = d.replace(year=datetime.now().year)
            return d.date()
        except ValueError:
            pass
    return None

@app.route("/neteja")
def neteja():
    titulo = "Gestió neteja setmanal"
    torns_rojos = {"AP", "B", "V", "FESTIU"}

    q = (request.args.get("q") or "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = 25

    query = NetejaSetmanal.query.filter(NetejaSetmanal.dia.isnot(None))

    if q:
        fecha = parse_date_q(q)

        if fecha:
            # -Buscar por día exacto
            query = query.filter(NetejaSetmanal.dia == fecha)

        else:
            # -Búsqueda por texto (lista blanca en NOM)
            allowed = {"M", "I", "L", "D", "EURO", "00NET"}

            q_norm = q.strip().upper().replace("\u00A0", "")
            nom_norm = func.upper(func.replace(NetejaSetmanal.nom, "\u00A0", ""))

            if q_norm in allowed:
                # -Si es un valor permitido: buscar SOLO por nom exacto
                query = query.filter(nom_norm == q_norm)
            else:
                # -Si no: búsqueda normal (nom o centre contiene)
                query = query.filter(
                    (NetejaSetmanal.nom.ilike(f"%{q}%")) |
                    (NetejaSetmanal.centre.ilike(f"%{q}%"))
                )

    pagination = query.order_by(
        NetejaSetmanal.dia.asc(),
        NetejaSetmanal.inici.asc(),
        NetejaSetmanal.id.asc()
    ).paginate(page=page, per_page=per_page, error_out=False)

    return render_template(
        "neteja/index.html",
        titulo=titulo,
        rows=pagination.items,
        pagination=pagination,
        q=q,
        torns_rojos=torns_rojos
    )

# ---------- MODELO ----------
class Claus(db.Model):
    __tablename__ = "claus"

    id = db.Column(db.Integer, primary_key=True)
    nom_porta = db.Column(db.String(255), nullable=False)
    nom_espai = db.Column(db.String(255), nullable=False)
    armari = db.Column(db.String(100), nullable=False)
    num = db.Column(db.Integer, nullable=False)
    
# ---------- /Claus ----------
@app.route("/claus")
def claus():
    titulo = "Gestió de claus"

    q = (request.args.get("q") or "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = 25

    query = Claus.query

    if q:
        query = query.filter(
            (Claus.nom_porta.ilike(f"{q}%")) |
            (Claus.nom_espai.ilike(f"{q}%")) |
            (Claus.armari.ilike(f"{q}%"))
        )

    pagination = query.order_by(
        Claus.nom_espai.asc(),
        Claus.nom_porta.asc(),
        Claus.num.asc(),
        Claus.id.asc()
    ).paginate(page=page, per_page=per_page, error_out=False)

    return render_template(
        "claus/index.html",
        titulo=titulo,
        rows=pagination.items,
        pagination=pagination,
        q=q
    )
# ---------- MODELO ----------    
class Todo(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    state = db.Column(db.Boolean, default=False)
    
# ---------- /TODO (LISTA) ----------
@app.route("/todo")
def todo_list():
    titulo = "Todo-list"

    q = (request.args.get("q") or "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = 25

    query = Todo.query
    if q:
        # -contiene (más cómodo que empieza por)
        query = query.filter(
            (Todo.title.ilike(f"%{q}%")) |
            (Todo.desc.ilike(f"%{q}%"))
        )

    # pagination = query.order_by(Todo.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    pagination = query.order_by(
        Todo.state.asc(),   # pendientes primero
        Todo.id.desc()      # dentro de cada grupo, las más nuevas arriba
        ).paginate(
    page=page, per_page=per_page, error_out=False
)

    return render_template(
        "todo/index.html",
        titulo=titulo,
        rows=pagination.items,
        pagination=pagination,
        q=q
    )


# ---------- /TODO (CREAR) ----------
@app.route("/todo/new", methods=["GET", "POST"])
def todo_new():
    titulo = "Nova tasca"

    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        desc = (request.form.get("desc") or "").strip()

        if title:
            todo = Todo(title=title, desc=desc, state=False)
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for("todo_list"))

    return render_template("todo/create.html", titulo=titulo)


# ---------- /TODO (EDITAR) ----------
@app.route("/todo/edit/<int:id>", methods=["GET", "POST"])
def todo_edit(id):
    todo = Todo.query.get_or_404(id)
    titulo = "Editar tasca"

    if request.method == "POST":
        todo.title = (request.form.get("title") or "").strip()
        todo.desc = (request.form.get("desc") or "").strip()
        todo.state = True if request.form.get("state") == "on" else False

        db.session.commit()
        return redirect(url_for("todo_list"))

    return render_template("todo/update.html", titulo=titulo, todo=todo)


# ---------- /TODO (BORRAR) ----------
@app.route("/todo/delete/<int:id>", methods=["POST"])
def todo_delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo_list"))



# ---------- CREAR TABLAS 1 VEZ ----------

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)


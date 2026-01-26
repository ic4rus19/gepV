
# !ARANQUE DE LA APLICACIÓN
# !flask --app app --debug run


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

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
@app.route("/neteja")
def neteja():
    titulo = "Gestió neteja setmanal"

    q = (request.args.get("q") or "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = 25

    query = NetejaSetmanal.query.filter(NetejaSetmanal.dia.isnot(None))

    if q:
        query = query.filter(
            (NetejaSetmanal.nom.ilike(f"{q}%")) |
            (NetejaSetmanal.centre.ilike(f"{q}%"))
        )

    pagination = query.order_by(
        NetejaSetmanal.dia.asc(),
        NetejaSetmanal.inici.asc(),
        NetejaSetmanal.id.asc()
    ).paginate(page=page, per_page=per_page, error_out=False)

    return render_template(
        "neteja.html",
        titulo=titulo,
        rows=pagination.items,
        pagination=pagination,
        q=q
    )


# ---------- CREAR TABLAS 1 VEZ ----------

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)


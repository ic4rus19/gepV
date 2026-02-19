from app import app, db, Claus

def main():
    with app.app_context():
        Claus.__table__.drop(db.engine, checkfirst=True)
        Claus.__table__.create(db.engine, checkfirst=True)
        print("✅ Tabla claus recreada con la nueva columna 'actuals' (Integer)")

if __name__ == "__main__":
    main()

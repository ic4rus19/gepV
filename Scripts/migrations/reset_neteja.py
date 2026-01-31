from app import app, db, NetejaSetmanal

def main():
    with app.app_context():
        # Borra SOLO la tabla neteja_setmanal
        NetejaSetmanal.__table__.drop(db.engine, checkfirst=True)
        # La vuelve a crear con la nueva columna 'torn'
        NetejaSetmanal.__table__.create(db.engine, checkfirst=True)

        print("✅ Tabla neteja_setmanal recreada con la columna 'torn'")

if __name__ == "__main__":
    main()

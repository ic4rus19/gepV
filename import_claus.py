
# -Importador de claus desde Excel.
# -Versión sin pandas (openpyxl).
# -Preparado para migrar a pandas en el futuro sin afectar a la app.

from openpyxl import load_workbook
from app import app, db, Claus  # IMPORTANTE

EXCEL_PATH = "data/claus.xlsx"

def main():
    wb = load_workbook(EXCEL_PATH)
    ws = wb.active

    # Cabeceras
    headers = [(str(c.value).strip().lower() if c.value else "") for c in ws[1]]
    required = ["nom_porta", "nom_espai", "armari", "num"]
    missing = [c for c in required if c not in headers]
    if missing:
        raise ValueError(f"Faltan columnas: {missing}. Detectadas: {headers}")

    idx = {h: headers.index(h) for h in required}

    rows_to_insert = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        nom_porta = r[idx["nom_porta"]]
        nom_espai = r[idx["nom_espai"]]
        armari = r[idx["armari"]]
        num = r[idx["num"]]

        if nom_porta is None and nom_espai is None and armari is None and num is None:
            continue

        nom_porta = str(nom_porta).strip() if nom_porta else None
        nom_espai = str(nom_espai).strip() if nom_espai else None
        armari = str(armari).strip() if armari else None

        try:
            num = int(num) if num is not None else 0
        except Exception:
            num = 0

        if not nom_porta or not nom_espai or not armari:
            continue

        rows_to_insert.append(
            Claus(
                nom_porta=nom_porta,
                nom_espai=nom_espai,
                armari=armari,
                num=num
            )
        )

    with app.app_context():
        Claus.query.delete()
        db.session.commit()

        db.session.bulk_save_objects(rows_to_insert)
        db.session.commit()

        print(f"✅ Import OK: {len(rows_to_insert)} filas a claus")

if __name__ == "__main__":
    main()

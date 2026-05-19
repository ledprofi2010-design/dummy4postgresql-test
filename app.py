import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        return "FEHLER: DATABASE_URL nicht gesetzt.", 500

    try:
        conn = psycopg2.connect(db_url)
        conn.close()
        return "Verbindung zur PostgreSQL-Datenbank erfolgreich!", 200
    except Exception as e:
        return f"Verbindung fehlgeschlagen: {e}", 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

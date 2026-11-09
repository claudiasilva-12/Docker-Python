import logging
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template

load_dotenv()

app = Flask(__name__)
logger = logging.getLogger(__name__)


def get_db_connection():
    """Establece conexión a la base de datos usando variables de entorno."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        dbname=os.getenv("DB_NAME", "datamart"),
        cursor_factory=RealDictCursor  # Retorna diccionarios en lugar de tuplas
    )


@app.route("/")
def index():
    """Página principal que muestra la tabla con el Ticket Promedio por Tienda."""
    resultados = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Consulta a la tabla que genera el pipeline MapReduce
        cursor.execute("SELECT tienda, ticket_promedio FROM resultados_ticket_promedio ORDER BY tienda;")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        logger.warning(f"No se pudo conectar o consultar la base de datos: {e}")

    return render_template("index.html", resultados=resultados)


@app.route("/api/resultados", methods=["GET"])
def get_resultados():
    """Endpoint REST JSON para exponer las métricas calculadas."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT tienda, ticket_promedio FROM resultados_ticket_promedio ORDER BY tienda;")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(resultados), 200
    except Exception as e:
        logger.error(f"Error al obtener resultados: {e}")
        return jsonify({"error": "No se pudieron obtener los datos"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

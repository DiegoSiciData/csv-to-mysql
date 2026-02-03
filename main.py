import csv
import logging
import mysql.connector
from config import DB_CONFIG

# Configuración logging
logging.basicConfig(
    filename="logs/errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def conectar_db():
    return mysql.connector.connect(**DB_CONFIG)

def limpiar_fila(fila):
    nombre = fila["nombre"].strip()
    email = fila["email"].strip()

    try:
        edad = int(fila["edad"])
    except ValueError:
        raise ValueError("Edad inválida")

    if not nombre or not email:
        raise ValueError("Nombre o email vacío")

    if "@" not in email:
        raise ValueError("Email inválido")

    return nombre, email, edad

def insertar_cliente(cursor, cliente):
    query = """
    INSERT INTO clientes (nombre, email, edad)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, cliente)

def procesar_csv(ruta_csv):
    conexion = conectar_db()
    cursor = conexion.cursor()

    with open(ruta_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            try:
                cliente = limpiar_fila(fila)
                insertar_cliente(cursor, cliente)
            except Exception as e:
                logging.error(f"Fila inválida {fila} | Error: {e}")

    conexion.commit()
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    procesar_csv("data/clientes.csv")
    print("Proceso finalizado.")

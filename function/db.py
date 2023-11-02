import sqlite3
# Direccion de la base de datos
db = "app/database/dispositivos.sqlite"

# Conectarse a la base de datos o crear una si no existe
conn = sqlite3.connect(f"{db}")

# Crear una tabla llamada "dispositivos" con tres columnas: "Nombre", "Tipo" e "IP"
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dispositivos (
        id INTEGER PRIMARY KEY,
        Nombre TEXT,
        Tipo TEXT,
        IP TEXT
    )
""")
conn.commit()
conn.close()

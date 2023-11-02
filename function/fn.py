from function.db import *
db = "app/database/dispositivos.sqlite"
# AGREGAR DISPOSITIVOS
def agregar_dispositivo(nombre, tipo, ip, db=f"{db}"):
    conn = sqlite3.connect(f"{db}")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dispositivos (Nombre, Tipo, IP) VALUES (?, ?, ?)", (nombre, tipo, ip))
    conn.commit()
    conn.close()

# REALIZAR CONSULTAS
def cantidad_total():
    conn = sqlite3.connect(f"{db}")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM dispositivos")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def cantidad_por_tipo():
    conn = sqlite3.connect(f"{db}")
    cursor = conn.cursor()
    cursor.execute("SELECT Tipo, COUNT(*) FROM dispositivos GROUP BY Tipo") # CORREGIR PARA SELECCIONAR EL TIPO
    result = cursor.fetchall()
    conn.close()
    return result

# EXPORTAR RESULTADOS
def exportar_resultados():
    resultados = cantidad_por_tipo()
    with open("app/resultados/resultados.txt", "w") as archivo:
        archivo.write("Cantidad Total: {}\n".format(cantidad_total()))
        archivo.write("Cantidad Por Tipo:\n")
        for tipo, cantidad in resultados:
            archivo.write("{}: {}\n".format(tipo, cantidad))
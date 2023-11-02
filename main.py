from function.db import *
from function.fn import *

# TEST:
# Agregar dispositivos
agregar_dispositivo("Dispositivo 1", "Tipo 1", "192.168.1.1")
agregar_dispositivo("Dispositivo 2", "Tipo 2", "192.168.1.2")

# Consultas
print("Cantidad Total:", cantidad_total())
print("Cantidad Por Tipo:")
for tipo, cantidad in cantidad_por_tipo():
    print(tipo, cantidad)

# Exportar resultados a un archivo de texto
exportar_resultados()

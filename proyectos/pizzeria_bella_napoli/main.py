from src.functions.añadir_orden import Añadir_orden
from src.functions.factura import Factura

hola = "hola mundo"

print("Bienvenido a Bella Napoli")
print("\n" + "-"*30 + "\n")
try:
    cantidad_sabores = int(input('Cantidad de sabores a elegir: '))
    if(cantidad_sabores<=2):
      Añadir_orden(cantidad_sabores)
except Exception as e:
    print('No se digita letras.')

Factura()
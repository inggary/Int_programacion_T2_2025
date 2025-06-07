
from src.database.db import orden

def Factura():
    if(len(orden)>0):
        print("\n------------------FACTURA--------------------\n")
        print(f'Su orden es: {", ".join(orden)}, mozzarella🧀 y tomate🍅. \nGracias por su compra.')
        print("\n---------------------------------------------\n")


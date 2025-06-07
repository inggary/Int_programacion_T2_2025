from src.functions.tools import Menu
from src.database.db import menu, orden

def Añadir_orden(cantidad_sabores):
    for repetir in range(1,cantidad_sabores+1):
        Menu(f'Para el sabor número: {repetir}.', list(menu.keys()))

        try:
            tipo_pizza_elegida = int(input('Elegir el número deseado: '))
            tipo_pizza_elegida = list(menu.keys())[tipo_pizza_elegida-1]

            Menu(f'Elegiste pizza {tipo_pizza_elegida}. \nIngredientes: \nMenu:', menu[tipo_pizza_elegida])
            ingrediente = int(input('Elegir el número deseado: '))
            orden.append(menu[tipo_pizza_elegida][ingrediente-1])
        except Exception as e:
            print('Opción no válida')
        print("\n--------------------------------------\n")


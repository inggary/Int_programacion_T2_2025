

# Ingredientes vegetarianos: Pimiento, tofu, Maiz, Queso, Hongos.
# Ingredientes no vegetarianos: Peperoni, Jamón, Salchicha Italiana, Tocino.

def Menu(titulo, lista):
    print("\n--------------------------------------\n")
    print(titulo)
    for numero, tipo  in enumerate(lista):
        print(f'{numero+1}. {tipo}')


ingredientes_vegetariana = ['pimiento', 'tofu', 'maiz', 'queso', 'hongos']
ingredientes_no_vegetariana = ['peperoni', 'jamon', 'salchicha italiana', 'tocino']
menu = {
    'vegetariana': ingredientes_vegetariana,
    'no vegetariana': ingredientes_no_vegetariana
}

orden = [] #'mozzarela y tomate'

print("Bienvenido a Bella Napoli")
print("\n" + "-"*30 + "\n")
try:
    cantidad_sabores = int(input('Cantidad de sabores a elegir: '))
    if(cantidad_sabores<=2):

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
except Exception as e:
    print('No se digita letras.')

if(len(orden)>0):
    print("\n------------------FACTURA--------------------\n")
    print(f'Su orden es: {", ".join(orden)}, mozzarella🧀 y tomate🍅. \nGracias por su compra.')
    print("\n---------------------------------------------\n")



# Ingredientes vegetarianos: Pimiento, tofu, Maiz, Queso, Hongos.
# Ingredientes no vegetarianos: Peperoni, Jamón, Salchicha Italiana, Tocino.

tipo_pizza = ['vegetariana', 'no vegetariana']
ingredientes_vegetariana = ['pimiento', 'tofu', 'maiz', 'queso', 'hongos']
ingredientes_no_vegetariana = ['peperoni', 'jamon', 'salchicha italiana', 'tocino']
orden = [] #'mozzarela y tomate'

print("Bienvenido a Bella Napoli")
print("\n" + "-"*30 + "\n")
cantidad_sabores = int(input('Cantidad de sabores a elegir: '))
if(cantidad_sabores<=2):

    for repetir in range(1,cantidad_sabores+1):
        print("\n--------------------------------------\n")
        print(f'Para el sabor número: {repetir}.')
        for numero, tipo  in enumerate(tipo_pizza):
            print(f'{numero+1}. {tipo}')
        tipo_pizza_elegida = int(input('Elegir el número deseado: '))

        print("\n--------------------------------------\n")
        #if(tipo_pizza-1==0):

        #comentario
        match(tipo_pizza_elegida-1):
            case 0:
                print('Elegiste pizza vegetariana. \nIngredientes vegetarianos: \nMenu:')

                for numero, ingrediente in enumerate(ingredientes_vegetariana):
                    print(f'{numero+1}. {ingrediente}')
                ingrediente = int(input('Elegir el número deseado: '))
                orden.append(ingredientes_vegetariana[ingrediente-1])

            case 1:
                print('Elegiste pizza no vegetariana. \nIngredientes no vegetarianos: \nMenu:')

                for numero, ingrediente in enumerate(ingredientes_no_vegetariana):
                    print(f'{numero+1}. {ingrediente}')
                ingrediente = int(input('Elegir el número deseado: '))
                orden.append(ingredientes_no_vegetariana[ingrediente-1])
            case _:
                print('Opción no válida')
        print("\n--------------------------------------\n")

print("\n------------------FACTURA--------------------\n")
print(f'Su orden es: {", ".join(orden)}, mozzarella🧀 y tomate🍅. \nGracias por su compra.')
print("\n---------------------------------------------\n")

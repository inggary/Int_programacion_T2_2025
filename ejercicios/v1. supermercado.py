Alimentos_Frescos = [
        "Tomates 🍅",
        "Lechuga romana 🥬",
        "Zanahorias 🥕",
        "Plátanos maduros 🍌",
        "Manzanas rojas 🍎",
        "Pechuga de pollo",
        "Carne molida de res",
        "Huevos 🥚",
        "Leche fresca 🥛",
        "Queso mozzarella 🧀"
    ]
Alimentos_Secos_Enlatados = [
        "Arroz integral 🍚",
        "Avena 🥣",
        "Pasta de trigo integral 🍝",
        "Lentejas 🌱",
        "Habichuelas negras (enlatadas o secas)",
        "Maíz dulce enlatado 🌽",
        "Atún enlatado 🐟",
        "Salsa de tomate 🥫",
        "Harina de trigo 🌾",
        "Azúcar morena 🍯"
    ]
Productos_Higiene_Limpieza = [
        "Papel higiénico 🧻",
        "Jabón de baño 🧼",
        "Champú y acondicionador 🧴",
        "Pasta dental 🦷",
        "Detergente para ropa 👕",
        "Suavizante de telas ✨",
        "Desinfectante multiusos 🦠",
        "Esponjas para lavar platos 🧽",
        "Toallas húmedas 🧻",
        "Bolsas de basura 🗑️"
    ]

productos_agotados = [
    "Pechuga de pollo",
    "Manzanas rojas 🍎",
    "Lechuga romana 🥬",
    "Arroz integral 🍚",
    "Atún enlatado 🐟",
    "Pasta de trigo integral 🍝",
    "Papel higiénico 🧻",
    "Detergente para ropa 👕",
    "Desinfectante multiusos 🦠",
]

lista_de_compras = []

lista_de_supermercado = [
    Alimentos_Frescos,
    Alimentos_Secos_Enlatados,
    Productos_Higiene_Limpieza
]


print("Bienvenido a La Sirena")
while(True):
    print("\n" + "-"*30 + "\n")
    print("""
    Elegir el número de la categoria a seleccionar
        1. Alimentos Frescos
        2. Alimentos Secos y Enlatados
        3. Productos de Higiene y Limpieza
        4. Finalizar compra
    """)
    categoria_seleccionada = int(input('Cual categoria usara(1-4): '))


    if((categoria_seleccionada > 3) & (categoria_seleccionada <= 0)):
        print('Opcion no valida')
    elif(categoria_seleccionada == 4):
        break
    else:
        while(True):
            categoria_seleccionada -= 1
            print("\n--------------------------------------\n")

            print(f'Elegir el producto a seleccionar:\n')

            for numero, tipo  in enumerate(lista_de_supermercado[categoria_seleccionada]):
                print(f'{numero+1}. {tipo}')
            articulo_seleccionado = int(input('Elegir el número deseado: '))

            if((articulo_seleccionado > len(lista_de_supermercado[categoria_seleccionada])) | (articulo_seleccionado <= 0)):
                print('Opcion no valida')
            elif(lista_de_supermercado[categoria_seleccionada][articulo_seleccionado-1] in productos_agotados):
                print('Producto agotado')
            else:
                lista_de_compras.append(lista_de_supermercado[categoria_seleccionada][articulo_seleccionado-1])
                break





    

print("\n------------------FACTURA--------------------\n")
print('Su orden es:')
for index, item in enumerate(lista_de_compras):
    print(f'{index+1}. {item}')
print('\n\nGracias por su compra.')
print("\n---------------------------------------------\n")

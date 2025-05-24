# Introducción a las estructuras de datos.

# Listas: Creación [], características (mutables, ordenadas).

lista_frutas = ['manzana', 'papa', 'uva', 'naranja', 'sandia'] 
#                   0       1          2       3         4

# Acceso a elementos: Índices (positivos y negativos).

#print(lista_frutas[-1])

# Modificación de elementos.

indice_papa = lista_frutas.index('papa') # esto es para encontrar 
                                         # el indice de un valor en la lista.
lista_frutas[indice_papa] = 'pera'

# print(lista_frutas[1])

# Slicing (rebanado) de listas.

#print(lista_frutas[::2])

# Funciones útiles: len().

# print(len(lista_frutas))

# Métodos de lista: append(), insert(), pop(), remove(), sort(), reverse(), etc.

# lista_frutas.append('aguacate') # agregar un valor a la lista
# print(lista_frutas)

# lista_frutas.insert(3, 'fresa') # agrega pero con indice
# print(lista_frutas)

# lista_frutas.pop(2) #borra un elemento y si no se pone nada borra el ultimo
# print(lista_frutas)

# lista_prueba = lista_frutas
# lista_prueba.sort(reverse=True) #reverse es para ordernar de mayor a menor
# print(lista_prueba)

# lista_frutas.reverse()
# print(lista_frutas)

# Iterar sobre listas con for.

# validador = ['manzana', 'banana', 'uva']

# for fruta in validador:
#     if( fruta in lista_frutas):    
#         print(fruta)
#     else:
#         print(f'{fruta} no esta disponible.')

# lista = [x for x in range(1,6)] # listas rapidas
# print(lista)

# validador = ['manzana', 'banana', 'uva']

# productos_disponibles = [fruta for fruta in validador if fruta in lista_frutas]
# productos_no_disponibles = [fruta for fruta in validador if fruta not in lista_frutas]

# print(f'Productos disponibles: {", ".join(productos_disponibles)}')
# print(f'Productos no disponibles: {", ".join(productos_no_disponibles)}')


# Diccionarios: Creación {clave: valor}, características (mutables, no ordenados antes de Python 3.7, acceso por clave).

# Operaciones con diccionarios: Acceder, añadir, modificar, eliminar elementos (del, pop()).

# Iterar sobre diccionarios (keys(), values(), items()).

# Tuplas: Creación (), características (inmutables, ordenadas). Casos de uso.

# Errores y Excepciones: ¿Qué pasa cuando el código falla?

# Manejo de excepciones: Bloques try y except. Capturar tipos específicos de error (ej: ValueError, TypeError, ZeroDivisionError).

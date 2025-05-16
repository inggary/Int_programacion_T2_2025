
# from random import randint

# ficha = randint(1, 6)

# # While - Este es un bucle que se utiliza cuando desconozco las veces que se repetira
# while( ficha != 3 ):

#     print(ficha)
#     ficha = randint(1, 6)

# print(f'ficha con el numero ganador: {ficha}')



# for - Es cuando conozco cuantas veces se repetira mi codigo

# for num1 in range(1, 6):

#     for num2 in range(1, 6):
#                     #x|=- decoración
#         print(f'{num1} x {num2} = {num1 * num2}')

#     print('-'*15)

# num = 5

# print(f'el numero {num}')

# print('el numero {nombre_de_la_variable}, {}'.format(10, nombre_de_la_variable=num))

# print('el numero %d' %(num))


# for num in range(1,11):
#     if(num % 2 == 0):
#         continue #saltar o volar esa repetición en curso
#     print(f'proximo numero: {num+1}')


# for num in range(1,11):
#     if(num == 6):
#         break #esto sirve como una pistola, mata el bucle
#     print(num)

# print('fin del bucle')


# while(True):

#     opcion = int(input("""
# Menu
#     1. Opcion 1
#     2. Opcion 2
#     3. Salir
# Elegir el numero correspondiente: """))

# # Suggested code may be subject to a license. Learn more: ~LicenseLog:2242580015.
#     match opcion:
#         case 1:
#             print('Elegiste la opcion 1')
#         case 2:
#             print('Elegiste la opcion 2')
#         case 3:
#             print('Elegiste la opcion 3 que es para salir')
#             break
#         case _:
#             print('Opcion incorrecta')



# for num in range(10,-1,-1):
#     print(f'usted es el numero {num}, espere en linea muy pronto sera atendido')


# while(True):

#     opcion = int(input("""
# Menu
#     1. Opcion 1
#     2. Opcion 2
#     3. Salir
# Elegir el numero correspondiente: """))

# # Suggested code may be subject to a license. Learn more: ~LicenseLog:2242580015.
#     match opcion:
#         case 1:
#             print('Elegiste la opcion 1')
#         case 2:
#             while(True):
#                 opcion2 = int(input("""
# Menu
#     1. Paquetico
#     2. Otra cosa
#     3. Volver
# Elegir el numero correspondiente: """))
#                 match opcion2:
#                     case 1:
#                         print('paquetico')
#                     case 2:
#                         print('otra cosa')
#                     case 3:
#                         print('Volver al menu anterior')
#                         break
#                     case _:
#                         print('Opcion incorrecta')
#         case 3:
#             print('Elegiste la opcion 3 que es para salir')
#             break
#         case _:
#             print('Opcion incorrecta')

#-----------------------------------
#tabla de la verdad

#conjucion
# print(False & True) #and - &

#disyucion
# print(False | False) #or - |

#negacion
# print(not False) #~ - not
#-----------------------------------

#signos de desigualdad

# print(5 > 6) #mayor que
# print(5 < 6) #menor que
# print(5 <= 6) #menor o igual
# print(5 >= 6) #mayor o igual
# print(5 == 6) #igual
# print(5 != 6) #diferente
# print('hola' > 'bebe')
# print(type(8.0)==float)


#-----------------------------------

#condicionales

#if-else

#JCE quiere un programa para automatizar la cedula de la persona

# FRANCHI = 2025 - 1900 # constante
# print(FRANCHI)

# if( (FRANCHI >= 18) & (FRANCHI < 125) ):
#     print('Cedula de mayor de edad.')
# elif((FRANCHI >= 16) & (FRANCHI < 125)):
#     print('Cedula de menor de edad.')
# elif((FRANCHI >= 0) & (FRANCHI < 125)):
#     print('No le toca cedula')
# else:
#     print('Fecha Erronea')


# tambien funciona de esta manera
# if(FRANCHI >= 18):
#     print('Cedula de mayor de edad.')
    # if(True):
    #     print('')
    # else:
    #     print('')
# else:
#     if(FRANCHI>=16):
#         print('Cedula de menor de edad.')
#     else:
#         print('No le toca cedula')

#match-case | switch-case

numero1 = 4
numero2 = 6
simbolo = '%'

match(simbolo):
    case '+':
        print(numero1+numero2)
        # if(True):
        #     print('')
        # else:
        #     print('')
    case '-':
        print(numero1-numero2)
    case '*':
        print(numero1*numero2)
    case '/':
        print(numero1/numero2)
    case _:
        print('No me enseñaron eso en la fabrica de programación.')

#-----------------------------------

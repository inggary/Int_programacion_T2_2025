
# funciones
def Suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

resultado = Suma(5,5)

def Hola():
    print("Hola Mundo")

#Hola()

def Suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado, numero1, numero2

resultado, n1, n2 = Suma(5,5)

#print(resultado)

#importacion de la libreria completa
#import math #libreria

#print(math.fabs(5))

#importacion de la libreria parcial
#from math import fabs as valor_absoluto, e, factorial #libreria

#print(valor_absoluto(-5))
#print(e)
#print(factorial(5))


import math as m #libreria

print(m.fabs(5))


def Menu(titulo, lista):
    print("\n--------------------------------------\n")
    print(titulo)
    for numero, tipo  in enumerate(lista):
        print(f'{numero+1}. {tipo}')

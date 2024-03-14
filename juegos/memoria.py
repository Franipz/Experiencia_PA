import random
def memoria():
    num = random.randint(10000,99999)
    print(num)
    secuencia = str(num)
    for i in range(15):
        print(" ")
    repuesta = input("Escribe la secuencia: ")
    if repuesta==secuencia:
        print("Lo lograste!!")
    else:
        print("Perdiste :(, la secuencia era", secuencia)
    

    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    pass
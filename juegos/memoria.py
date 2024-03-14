import random
def memoria():
    secuencia = ""
    for i in range(10):
        num = random.randint(0,9)
        print(num)
        secuencia += str(num)
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
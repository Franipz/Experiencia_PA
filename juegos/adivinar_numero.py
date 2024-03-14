import random
def adivinar_numero():
    num = int(input("Ingresa un numero del 1 al 10: "))
    minum = random.randint(1,10)
    if num == minum :
        print("Muy bien, adivinaste!")
    else:
        print("Ese no es el número :(, era", minum)

    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    pass
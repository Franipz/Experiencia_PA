import random
def adivinar_par_o_impar():
    poi = input("¿Par o impar?: ")
    minum = random.randint(1,100)
    if poi == "par" and minum%2 == 0:
        print("Muy bien, adivinaste! El numero era", minum)
    elif poi == "impar" and minum%2 != 0:
        print("Muy bien, adivinaste! El numero era", minum)

    else:
        print("No adivinaste :(, el numero era", minum)
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """

    pass
import random
def cachipun():
    opciones=["piedra", "papel", "tijera"]
    num = random.randint(0,2)
    eleccion = input("¿piedra, papel o tijera?:")
    print(eleccion,"vs",opciones[num])
    if eleccion == opciones[num]:
        print("Empate!")
    elif eleccion == "piedra":
        if opciones[num] == "papel":
            print("Perdiste :(")
        else:
            print("Ganaste!")
    elif eleccion == "papel":
        if opciones[num] == "tijera":
            print("Perdiste :(")
        else:
            print("Ganaste!")
    elif eleccion == "tijera":
        if opciones[num] == "piedra":
            print("Perdiste :(")
        else:
            print("Ganaste!")
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    pass
import random
def juego_del_dado():
    enter = input("Apreta enter para empezar: ")
    mipuntaje=0
    cpuntaje=0
    while mipuntaje < 30 and cpuntaje < 30:
        dado1=random.randint(1,6)
        mipuntaje += dado1
        print("Tu puntaje:",mipuntaje)
        dado2 = random.randint(1,6)
        cpuntaje += dado2
        print("Puntaje oponente:",cpuntaje)
    if mipuntaje >= 30:
        print("Ganaste!")
    else:
        print("Perdiste")
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    pass
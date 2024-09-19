import random

def datos():
    turnos = int(input("Numero de turnos para tirar: "))
    puntos = 0
    puntos2 = 0
    for turnos in range(turnos):
        print(f"\n Ronda: {turnos + 1}")
        dadoJugador = random.randint(1,6)
        dadoJugador2 = random.randint(1,6)    
        input("Enter para ver la ronda: ")
        print(f"La primera persona sacó: {dadoJugador}")
        print(f"La segunda persona sacó: {dadoJugador2}")

        if dadoJugador > dadoJugador2:
            print(f"El primer jugador ganó esta ronda con: {dadoJugador}")
            puntos += 1
        elif dadoJugador2 > dadoJugador:
            print(f"El segundo jugador ganó esta ronda con: {dadoJugador2}")
            puntos2 += 1
        else:
            print("Salio empate de datos :")
            print(f"{dadoJugador} y {dadoJugador2}")
    print("\n Tabla de puntaje: ")
    print(f"Puntos primer Jugador: {puntos}")
    print(f"Puntos segundo Jugador: {puntos2}")

    if puntos > puntos2:
        print("El primer jugador ganó el juego")
    elif puntos2 > puntos:
        print("El segundo jugador ganó el juego")
    else:
        print("El juego quedó en empate")

datos()
def calcularMaxMin(lista):
    return (max(lista),min(lista)) if lista else None

def ingresarNumeros():
    numeros = []
    while True:
        numero = input("Ingresa los numeros que quieras, para pararlo pon 'salir' ")
        if numero.lower() == "salir":
            break
        try:
            numeros.append(int(numero))
        except ValueError:
            print("Solo se permiten números")

    if numeros:
        maximo, minimo = calcularMaxMin(numeros)
        print(f"Máximo: {maximo}, Minimo {minimo}")
    else:
        print("No se ingresó ningun número")

ingresarNumeros()
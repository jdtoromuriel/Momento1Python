def calcularMaxMin(lista):
    return (max(lista),min(lista)) if lista else None

listaNumeros = [15,80,90,1,2,4,125,0,8]

maximo, minimo = calcularMaxMin(listaNumeros)

print("Máximo", maximo)
print("Minimo", minimo)
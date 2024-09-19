import math

def suma():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    resultado = a + b
    print("El resultado de la suma es:", resultado)
    
def resta():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    resultado = a - b
    print("El resultado de la resta es:", resultado)
    
def multiplicacion():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    resultado = a * b
    print("El resultado de la multiplicacion es:", resultado)
    
def division():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    if b == 0:
        print("No se puede dividir por 0")
    else:
        resultado = a / b
        print("El resultado de la division es:", resultado)
        
def potenciacion():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    resultado = a ** b
    print("El resultado de la potenciacion es:", resultado)
    
def factorial():
    a = int(input("Ingrese el valor: "))
    resultado = math.factorial(a)
    print("El resultado del factorial es:", resultado)
    
def raizCuadrada():
    a = int(input("Ingrese el valor: "))
    resultado = math.sqrt(a)
    print("El resultado de la raiz cuadrada es:", resultado)

def calculadora():
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potenciacion")
    print("6. Factorial")
    print("7. Raiz cuadrada")
    print("8. Salir")
    opcion = int(input("Ingrese la operacion que desea realizar: "))
    while opcion != 8:
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            potenciacion()
        elif opcion == 6:
            factorial()
        elif opcion == 7:
            raizCuadrada()
        else:
            print("Opcion no valida")
        opcion = int(input("Ingrese la operacion que desea realizar: "))
    print("Gracias por usar la calculadora")
    
calculadora()
import math

def supCirculo(radio):
    supm2 =  math.pi* (radio**2)
    return(supm2)

def supRectangulo(base,altura):
    supm2 = base * altura
    return(supm2)

def supTriangulo(base,altura):
    supm2 = base * altura / 2
    return(supm2)

while True:

    print("Hola! Bienvenido al calculador de superficies (en m2).")
    print("¿Qué Figura le gustaría calcular?")
    print("1.Círculo")
    print("2.Triángulo")
    print("3.Rectángulo")
    print("Cualquier otra tecla: Salir")
    figura = int(input())


    if figura == 1:
        print("¿Cuál es el radio del círculo (metros)?")
        radio = float(input())
        superficie = supCirculo(radio)
        print("La superficie del círculo es de " + str(superficie) + "m2.\n")

    elif figura == 2:
        print("¿Cuál es la base del triángulo (metros)?")
        base = float(input())
        print("¿Cuál es la altura del triángulo (metros)?")
        altura = float(input())
        superficie = supTriangulo(base,altura)
        print("La superficie del triángulo es de " + str(superficie) + "m2.\n")

    elif figura == 3:
        print("¿Cuál es la base del rectángulo (metros)?")
        base = float(input())
        print("¿Cuál es la altura del triángulo (metros)?")
        altura = float(input())
        supRectangulo(base,altura)
        print("La superficie del rectángulo es de " + str(superficie) + "m2.\n")

    else:
        print("Gracias por utilizar el calculador de superficies.")
        break
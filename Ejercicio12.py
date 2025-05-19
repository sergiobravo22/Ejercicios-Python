# Programa que solicite cuatro valores numéricos enteros e informar su suma y promedio.

try:
    numeros = []

    for i in range(1,5):
        teclado = int(input("Coloca un número: "))
        numeros.append(teclado)

    print("La suma de todos es: {0}".format(sum(numeros)))
    print("Su promedio es de: {0}".format(sum(numeros) / len(numeros)))

except ValueError:
    print("Debes colocar solamente numeros... {0}".format(ValueError))
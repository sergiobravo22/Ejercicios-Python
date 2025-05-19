# Obtener suma y resta de dos números ingresados.

try:
    numeros = []

    for i in range(1,3):
        teclado = int(input("Coloca un numero: "))
        numeros.append(teclado)
    print("La suma es: ", (numeros[0] + numeros[1]))
    print("La resta es: ", (numeros[0] - numeros[1]))

except ValueError:
    print("Coloca solamente numeros ({})".format(ValueError))
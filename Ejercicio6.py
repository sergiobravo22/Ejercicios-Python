# Intercambiar los valores de 2 variables numéricas.

try:
    numeros = []

    for i in range(1,3):
        teclado = float(input("Coloca un numero: "))
        numeros.append(teclado)

    a = numeros[0]
    b = numeros[1]

    print("Los primeros numeros son a = {0} | b = {1}".format(a,b))
    a,b = b,a
    print("Luego, intercambian a = {0} | b = {1}".format(a,b))


except ValueError:
    print("Debes colocar solamnete numeros... {0}".format(ValueError))
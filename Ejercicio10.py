# Calcular A + B / C + D

try:
    print("Coloca cuatro valores: ")
    numeros = []
    for i in range(1,5):
        teclado = int(input("Debes colocar un número: "))
        numeros.append(teclado)
    serie_a = [numeros[0], numeros[1]]
    serie_b = [numeros[2], numeros[3]]
    total_a = sum(serie_a)
    total_b = sum(serie_b)
    print("El cálculo {0}+{1}/{2}+{3} = {4}".format(numeros[0],numeros[1],numeros[2],numeros[3],(total_a/total_b)))



except ValueError:
    print("Debes colocar solamente números... {0}".format(ValueError))
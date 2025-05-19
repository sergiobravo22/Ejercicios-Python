# Calcular el promedio de tres números ingresados


try:
    lista_numeros = []
    for i in range(1, 4):
        teclado = int(input("coloca tres numeros: "))
        lista_numeros.append(teclado)

    promedio = sum(lista_numeros)

    if lista_numeros == 0:
        print("El promedio es 0.")

    else:
        print("el promedio es de: ", promedio/len(lista_numeros))

except (TypeError, ValueError):
    print("Debes colocar numeros y no letras/palabras...")




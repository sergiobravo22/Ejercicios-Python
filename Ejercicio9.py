# Calcular (x + y)²

try:
    numeros=[]
    for i in range(1,3):
        teclado = float(input("Coloca un número: "))
        numeros.append(teclado)
    print("El resultado de ({0}+{1})**2 es de: {2}".format(numeros[0],numeros[1],((numeros[0]+numeros[1])**2)))

except ValueError:
    print("Debes colocar solamente numeros... {0}".format(ValueError))
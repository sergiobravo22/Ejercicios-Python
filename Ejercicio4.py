# Calcular el perímetro de un triángulo rectángulo, dadas la base y la altura.
import math

try:
    numeros = [] #index(0) = base | index(1) altura
    print ("Debes colocar dos numeros, representan a la base y altura de un triangulo...")
    for i in range(1,3):
        teclado = float(input("Coloca un numero: "))
        numeros.append(teclado)
    calculo = math.sqrt(numeros[0]+numeros[1])

    print("Teniendo los valores de 'b' y 'h' ({0},{1}), El perímetro es: {2}".format(numeros[0],numeros[1],calculo))

except ValueError:
    print("Debes colocar solamente numeros... {0}".format(ValueError))
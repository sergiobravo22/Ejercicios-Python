# Para un numero x dado, calcular x3.

try:
    teclado = float(input("Coloca un numero: "))
    print(teclado**3)

except ValueError:
    print("Debes colocar solamente numeros... {0}".format(ValueError))
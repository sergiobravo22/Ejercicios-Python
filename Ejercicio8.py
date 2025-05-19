# Calcular el valor a pagar por tres productos y el IVA pagado para los tres.
# Recordar que el IVA aplicado es el 21%.

try:
    numeros=[]
    print("Coloca tres valores para sacar el IVA total")
    for i in range(1,4):
        teclado = float(input("Coloca un numero: "))
        numeros.append(teclado)
    iva = (sum(numeros)*21)/100
    print("--- PRODUCTOS ---")
    print("1° Producto: ${0}".format(numeros[0]))
    print("2° Producto: ${0}".format(numeros[1]))
    print("3° Producto: ${0}".format(numeros[1]))
    print("-----")
    print("IVA 21%: ${0}".format(iva))
    print("-----")
    print("Total: ${0}".format(sum(numeros)+iva))

except ValueError:
    print("Debes colocar solamente numeros... {0}".format(ValueError))
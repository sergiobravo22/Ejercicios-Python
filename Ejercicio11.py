# Desarrollar un programa que solicite el ingreso del precio de un artículo y la cantidad que lleva el
# cliente. Mostrar lo que debe abonar el comprador.

try:
    precio = float(input("Coloca el precio del producto: $"))
    cantidad = int(input("Coloca la cantidad del producto: "))

    print("El precio es de ${0}".format((precio*cantidad)))

except ValueError:
    print("Debes colocar solamente numeros... {0}".format(ValueError))
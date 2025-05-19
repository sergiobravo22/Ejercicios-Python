# Algoritmo que convierta las longitudes del sistema inglés al sistema métrico decimal.
# Tener en cuenta que 1 milla = 1.609344 km 1 pie = 30.48 cm - 1 pulgada = 2.54 cm

while True:
    try:
        print("------ ELIGE UNA OPCIÓN ------")
        print("(1) Sistema inglés al métrico decimal.")
        print("(2) Sistema métrico decimal al inglés.")
        print("(3) Salir.")
        print("------------------------------")
        teclado = int(input("Coloca tu opción: "))

        if teclado == 1:
            print("------ ELIGE UNA OPCIÓN ------")
            print("(1) pulgadas a centímetros.")
            print("(2) pies a centímetros.")
            print("(3) milla a kilómetros.")
            print("(4) Salir.")
            print("------------------------------")
            teclado = int(input("Elige una opción: "))

            if teclado == 1:
                teclado = float(input("Coloca la cantidad de pulgadas: "))
                print("La cantidad es de {0} cm.".format((teclado*2.54)))
                break
            if teclado == 2:
                teclado = float(input("Coloca la cantidad de pies: "))
                print("La cantidad es de {0} cm.".format((teclado * 30.48)))
                break
            if teclado == 3:
                teclado = float(input("Coloca la cantidad de millas: "))
                print("La cantidad es de {0} km.".format((teclado*1.609344)))
                break
            if teclado == 4:
                print("¡Muchas gracias por usar nuestro programa!")
        if teclado == 2:
            print("------ ELIGE UNA OPCIÓN ------")
            print("(1) centímetros a pulgadas.")
            print("(2) centímetros a pies.")
            print("(3) kilómetros a millas.")
            print("(4) Salir.")
            print("------------------------------")
            teclado = int(input("Elige una opción: "))

            if teclado == 1:
                teclado = float(input("Coloca la cantidad de centimetros a pulgadas: "))
                print("La cantidad es de {0} pulgadas.".format((teclado/2.54)))
                break
            if teclado == 2:
                teclado = float(input("Coloca la cantidad de centimetros a pies: "))
                print("La cantidad es de {0} pies.".format((teclado / 30.48)))
                break
            if teclado == 3:
                teclado = float(input("Coloca la cantidad de millas a kilómetros: "))
                print("La cantidad es de {0} millas.".format((teclado/1.609344)))
                break
            if teclado == 4:
                print("¡Muchas gracias por usar nuestro programa!")
                break
        if teclado == 3:
            print("¡Gracias por usar nuestro programa!")
            break
        else:
            print("coloca valores correctos...")
            continue
    except ValueError:
        print("Debes colocar solamente números... {0}".format(ValueError))

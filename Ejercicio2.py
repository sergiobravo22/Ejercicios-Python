# Calcular el área de una circunferencia, dada la medida de su radio.
# area = pi * R**2

try:
    radio = int(input("Coloca el radio de la circunferencia: "))

    print("La circunferencia es de: ", 3.14159265 * (radio**2))


except (ValueError, TypeError):
    print("Coloca solamente números...")

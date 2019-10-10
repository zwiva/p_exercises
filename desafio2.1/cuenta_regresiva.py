cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
i = cuenta_regresiva
while i > 0:
    i -= 1 # next countdown
    print("Iteración {}".format(i+1))

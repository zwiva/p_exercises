n = int(input("Ingrese un número para sumar sus pares\n"))
i = 1
suma = 0
for i in range(1, n+1):
    if i % 2 == 0:
        suma +=i
print(suma)
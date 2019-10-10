n = int(input("Ingrese un número para identificar sus pares\n"))
i = 1
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
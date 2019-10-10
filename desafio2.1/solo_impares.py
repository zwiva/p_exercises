n = int(input("Ingrese un número para identificar sus impares\n"))
i = 0
for i in range(n+1):
    if i % 2 != 0:
        print(i)
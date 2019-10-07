from sys import argv
import random
list = [1,2,3]
jugada = argv[1]
computador = random.choice(list)
if computador == 1:
    opcion = "piedra"
elif computador == 2:
    opcion = "papel"
else:
    opcion = "tijera"
if jugada == opcion:
    print("Computador juega {}".format(opcion))
    print("Empataste")
elif jugada == "papel" and opcion == "piedra" or jugada == "piedra" and opcion == "tijera" or jugada == "tijera" and opcion == "papel": 
    print("Computador juega {}".format(opcion))
    print("Ganaste")
elif jugada == "papel" and opcion == "tijera" or jugada == "piedra" and opcion == "papel" or jugada == "tijera" and opcion == "piedra":
    print("computador juega {}".format(opcion)) 
    print("Perdiste")
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
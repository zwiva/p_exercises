# Crear el programa emprendedor1.py donde el usuario ingrese el precio, el número de usuarios y los gastos. El programa debe calcular y mostrar las utilidades.

import sys

p = float(sys.argv[1])
u = float(sys.argv[2])
g = float(sys.argv[3])

util = (p * u) - g

#refactorizado
if util > 0:
    util = util * 0.65

print("la utilidad es {}".format(util))

# version larga:
# if util > 0:    
#     print("la utilidad es {}".format(util - (util*0.35)))
# else:
#     print("la utilidad es negativa")



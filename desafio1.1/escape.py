import sys
import math

g = float(sys.argv[1]) #recibe primer parametro
r = float(sys.argv[2]) #recibe segundo parametro
x = (2 * g * r * 1000)
print("La velocidad de escape es {}".format(math.sqrt(x)))
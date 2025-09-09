import MiBilblio as mb
import numpy as np


salida = open("fibonachos.txt",'w')

Nachos = mb.fibonacci(100000)

for i in Nachos:
    salida.write("%i \t" % i)
salida.close()

secuencia = np.loadtxt("fibonachos.txt")

print(sum(secuencia))

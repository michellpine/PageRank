import numpy as np
import time
import sys

#Validacion de los argumentos
if len(sys.argv) != 4:
    print 'Ingrese: '+sys.argv[0]+' <nodos> <densidad> <tolerancia>'
    exit(1)

#Validando tipo de datos en los argumentos
try:
    N = int(sys.argv[1]) #Nodos
    d = float(sys.argv[2]) #densidad
    e = float(sys.argv[3]) #tolerancia
except:
    print 'Ingrese el tipo de dato correcto'
    exit(1)

vectorR = []

def pageRank(vector):
    print vectorR

def matrizEstocastica(nodos, densidad):
    t = time.time()
    matriz = []
    return matriz
	
def hallarVectorR(N, d, e):
    matrizA = matrizEstocastica(N, d)
    resul = pageRank(vectorR) 

    print "time: {}".format(time.time() - t)

hallarVectorR(N, d, e)

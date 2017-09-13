import pylab as plt
#para graficar vectores# 
import numpy as num 
#para usar la propiedad arange#
x=num.arange(0,22)
#usando arange se evita escribir cada numero#
#Va de uno en uno desde 0 a 22#
y=num.arange(1995,2017)
#Va de uno en uno desde 19995 a 2017#
plt.plot(x,y)
#Grafica cada 'arange'#
plt.xlabel('edad')
plt.ylabel('anio')
#etiquetas de cada eje#
plt.savefig('ejercicio1')
#generacion de la imagen#

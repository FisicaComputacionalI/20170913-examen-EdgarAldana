import pylab as plt
#graficador#
import numpy as np
#para la funcion seno#
x=np.arange(0.0,3.0,0.1)
#La grafica ira de 0 a 3, debido a que la magnitud(3) es el numero de años que llevo en la universidad#
#La magnitud de una función trigonometrica es el n'umero que va multiplicado a la funci'on no el rango. 
#Una definici'on m'as apropiada ser'ia 3*np.cos(2*np.pi*t)+2014
plt.plot(x,2014*(np.sin(x)))
#la constante 2014 en el eje y#
plt.savefig('ejercicio2')
#guarda la imagen#

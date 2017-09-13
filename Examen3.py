import numpy as np 
#para la funcion seno y el arange#
import matplotlib.pyplot as plt 
#para graficar dos figuras#

#Sigue el codigo para graficar la misma figura del ejercicio 1#
plt.figure(1)
plt.subplot(211)
x=np.arange(0,22)
y=np.arange(1995,2017)
plt.plot(x,y,'b')
#Color azul:'b'#
plt.xlabel('edad')
plt.ylabel('anio')

#Codigo para graficar la misma figura del ejercicio 2#
plt.subplot(212)
x=np.arange(0.0,3.0,0.1)
plt.plot(x,2014*(np.sin(x)),'g')
#Color verde: 'g'#

#Guardar y mostrar figura#
plt.savefig('ejercicio3.png')
plt.show()

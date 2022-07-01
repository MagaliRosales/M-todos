#derivacion e integración de funciones

from sympy import Symbol
from scipy.misc import derivative
x=Symbol('x')
#funcion a derivar es 2x^3
y=2*x**3
derivada=y.diff(x)
print(derivada) #resultado de la derivada en función

f=lambda x: 2*x**3
#1.0 el valor en el que se evalua. dx=1e-6 valor del espaciado
print(derivative(f,1.0,dx=1e-6))#resultado derivado

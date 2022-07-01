#integracion de funciones

from sympy import Symbol
from sympy import integrate
from scipy.integrate import quad

x=Symbol('x')
#la funcion es x^3+x^2+1
print (integrate(x**3+x**2+1,x))
f=lambda x:x**3+x**2+1
#limite menor es 1 y el mayor 2
print (quad(f,1,2))
#el primer valor es la integral y el segundo el error

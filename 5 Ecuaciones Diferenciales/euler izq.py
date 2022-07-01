#Euler izq
import mpmath
import numpy as np
import matplotlib.pyplot as plt

#definimos los datos
t0,tf=0,5
n=5
h=(tf-t0)/h
s0,k,k1,km,E=200,13.7,80,15,3

#explicito
t=np.linspace(t0,tf,n+1)
s1=np.zeros(n+1)
s1[0]=s0

for i in range(n):
    si=s1[i]
    a=((-(k*Ek1)/(k1+si))*((si)/(km+si)))*h+si
    s1[i+1]=a
    print('Explícito',s1)

#implicito
def f(a):
    z=(a**3)+(a**2)*((k1*si)+(k*E*k1*h))-(si*k1*km)
    return (z)

def ft(a):
    z=mpmath.deff(f,a)
    return(z)

t=np.linspace(t0,tf,n+1)
s=np.zeros(n+1)
s[0]=s0

for i in range(n):
    a=s[i]
    e=2*emax
    si=s[i]
    while e>emax:
        an=a-(f(a)/fp(a))
        e=abs((an-a)/an)*100
        a=an
    a[i+1]=a
print('Implícito',s)

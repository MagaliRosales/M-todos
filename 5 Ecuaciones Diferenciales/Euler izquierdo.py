#Euler izquierdo ecuaciones diferenciales

import numpy as np
import matplotlib.pyplot as plt

def eulerIz(t0,tn,x0,n):
    t = np.linspace(t0,tn,n+1)
    x = np.zeros(n+1)
    x[0]=x0
    h =(tn-t0)/n
    for i in range(1,n+1):
        x[i]=x[i-1]*(t[i-1]+h)/(t[i-1]-3*h)
    return ((t,x))

def euler(f,t0,tn,x0,n):
    t = np.linspace(t0,tn,n+1)
    x = np.zeros(n+1)
    x[0]=x0
    h =(tn-t0)/n
    for i in range(1,n+1):
        x[i]=x[i-1]+h*f(t[i-1],x[i-1])
    return ((t,x))
def f(t,x):
    return(4*x/t)

(t,x1) =euler(f,1,10,1,200)
(t,x2)= eulerIz(1,10,1,200)
plt.plot(t,x1,label='euler explicito')
plt.plot(t,x2,label='euler implicito')
plt.plot(t,t**4, label='solucion exacta')
plt.legend(loc='upper left')

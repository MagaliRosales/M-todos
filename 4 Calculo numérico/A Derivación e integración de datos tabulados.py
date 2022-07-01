# Derivada
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**3+2*x**2+5*x+1

N=11
a=-2
b=2
x=np.linspace(a,b,N)
dx=(b-a)/(N-1)

y=f(x)
yp=np.zeros_like(x)

for i in range(N):
    if i==0:  #primer dato
        yp[i]=(y[i+1]-y[i])/dx #derivada hacia delante
    elif i==N-1:  #ultimo dato. 
        yp[i]=(y[i]-y[i-1])/dx  #realiza derivada hacia atras
    else:
        yp[i]=(y[i+1]-y[i])/(2*dx) #derivada Central

def fp(x):
    return 9*x**2+4*x+5
plt.plot(x,fp(x),'g-')
plt.plot(x,yp,'bo')
plt.show()

#metodo Runge Kutta 4to orden de ecuaciones diferenciales

def runge(f,xo,yo,paso,xf):
    y=[yo]
    x=[xo]
    h=paso
    n=int((xf-xo)/h)
    for i in range(1,n+1):
        xi=x[i-1]
        yi=y[i-1]
        k1=f(xi,yi)
        k2=f(xi+h/2,yi+1/2*h*k1)
        k3=f(xi+h/2,yi+1/2*k2*h)
        k4=f(xi+h,yi+k3*h)
        x.append(xi+h) # a x colocamos el valor de xi
        y.append(yi+1/6*h*(k1+2*k2-2*k3*k4))
    return x,y

func=lambda x,y:2*x*y
x,ye=runge(func,1,1,0.1,1.5)
print(x,ye)

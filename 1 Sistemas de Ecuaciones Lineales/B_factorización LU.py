#Factorizacion LU

import numpy as np
print ("Descomposición LU, matrices cuadradas")
m= int (input("Introduce el número de renglones"))

#Inicializamos las matrices con ceros
matriz=np.zeros([m,m])
u=np.zeros([m,m])
l=np.zeros([m,m])
#Introducimos los elementos de la matriz
print("Inrtoduce la matriz")
#ciclos anidados
for r in range(0,m): #filas
    for c in range(0,m): #columnas
        #almacenamos la matriz
        matriz[r,c]=(input("Elemento a["+str(r+1)+","+str(c+1)+"]"))
        matriz[r,c]=float(matriz[r,c])
        u[r,c]=matriz[r,c]
#Eliminacion de gauss, ceros en al diagonal principal
for k in range(0,m):
    for r in range (0,m):
        if(k==r):
            l[k,r]=1
        if (k<r):
            factor=(matriz[r,k]/matriz[k,k])
            l[r,k]=factor
            for c in range(0,m):
                matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
                u[r,c]=matriz[r,c]
print("resultado")
print("Matriz L")
print(l)
print("Matriz U")
print(u)      

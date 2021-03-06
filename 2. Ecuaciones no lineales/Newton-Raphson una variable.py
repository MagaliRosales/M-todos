#Newton/Raphson 1 variable


import numpy as np
import matplotlib.pyplot as plt
#definimos la funcion
def F(x):
    return x**2 - 2
 
def dFdx(x):
    return 2*x



#metodo newton
rootValues = [4.0] # valor inicial
error = 0.001
rootGuess = rootValues[-1]
print ("%11s %11s" % ("x", "F(x)"))
while True:
    print ("%11.8f %11.8f" % (rootGuess, F(rootGuess)))
    droot = -1*F(rootGuess)/dFdx(rootGuess)
    rootGuess = rootGuess + droot
    rootValues.append(rootGuess)
    if abs(rootValues[-2] - rootValues[-1]) < error:
        break
rootValues = np.array(rootValues)
x = np.linspace(0,5,100)
plt.figure(num="Newton")
plt.clf()
plt.plot(x, F(x))
plt.plot(rootValues, F(rootValues), 'ko', ms=6)
plt.grid('on')
plt.show()

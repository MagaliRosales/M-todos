# Interpolaciones cubicas

import numpy as np
f1=[-8,4,-2,1,0,0,0,0,0,0,0,0];
f2=[-1,1,-1,1,0,0,0,0,0,0,0,0];
f3=[0,0,0,0,-1,1,-1,1,0,0,0,0];
f4=[0,0,0,0,1,1,1,1,0,0,0,0];
f5=[0,0,0,0,0,0,0,0,1,1,1,1];
f6=[0,0,0,0,0,0,0,0,27,9,3,1];
f7=[3,-2,1,0,-3,2,-1,0,0,0,0,0];
f8=[0,0,0,0,3,2,1,0,-3,-2,-1,0];
f9=[-6,2,0,0,6,-2,0,0,0,0,0,0];
f10=[0,0,0,0,6,2,0,0,-6,-2,0,0];
f11=[-12,2,0,0,0,0,0,0,0,0,0,0];
f12=[0,0,0,0,0,0,0,0,18,2,0,0];
b=[3,1,1,2,2,-1,0,0,0,0,0,0]

A=np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12])
x=np.linalg.solve(A,b)
print("los coeficiontes son")
print(x)

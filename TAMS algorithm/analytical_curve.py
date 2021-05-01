import numpy as np
import matplotlib.pyplot as plt
from math import *

def Fun(x):
    value= exp(pow(x,2)) * pow((1+erf(x)),2)

    return(value)

def Return_time(a):
    X=np.linspace(-10,a,num=100000)
    dX=X[1]-X[0]
    T=0
    for ele in X:
        T=T+Fun(ele)*dX

    return(T*sqrt(pi)/2)


A_value=np.linspace(1,6,num=100)
T_value=[]
for m in A_value:
    T_value.append(Return_time(m))

np.save('a_theory.npy', A_value)
np.save('t_theory.npy', np.log10(T_value))

#plt.plot(np.log10(T_value),A_value)
#plt.grid(True)
#plt.show()


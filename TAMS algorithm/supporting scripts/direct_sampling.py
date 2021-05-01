import numpy as np
import matplotlib.pyplot as plt
from math import *

alpha=1
e_value= 0.5
t=100000
N=1000*t

def Dir_est(a):
    a_crit=a
    Tcrit=0
    Tdiff=[]
    X = np.zeros(N)
    X[0]=np.random.normal(0,sqrt(0.5))
    T=np.linspace(0,t,num=N)
    dt= T[1]-T[0]
    c=0
    i=1
    while i<N:
        X[i] = X[i-1] - alpha*X[i-1]*dt + sqrt(dt*2*e_value)*np.random.normal()
        if c==0:
            if X[i]>=a_crit:
                Tdiff.append(T[i]-Tcrit)
                Tcrit=T[i]
                c=1
        else:
            if X[i]<a_crit:
                c=0

        i=i+1

    T_tot=0
    for ele in Tdiff:
        T_tot = T_tot + ele*ele/2

    return(T_tot/t)

A_value=np.linspace(1.5,3.5,num=9,endpoint=True)
T_value=[]
m=0
while m<len(A_value):
    To=Dir_est(A_value[m])
    if To:
        T_value.append(log10(To))
        m=m+1

np.save('a_direct.npy', A_value)
np.save('t_direct.npy', T_value)

#plt.plot(T_value,A_value)
#plt.grid(True)
#plt.show()

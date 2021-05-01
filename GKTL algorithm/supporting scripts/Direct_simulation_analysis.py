import numpy as np
import matplotlib.pyplot as plt
from math import *
import seaborn as sns

alpha=1
epsilon= 0.5
Ta=100000
T_obs=50
dt=1/1000
N=int(Ta/dt)
tau=100

def running_mean(x, N):
    """ x == an array of data. N == number of samples per average """
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)



Xs=np.load('series.npy')

X_avg=running_mean(Xs,int(T_obs/dt))

X_blocks=[]
for i in range((int((Ta-T_obs)/tau))+1):
    start=int(i*tau/dt)
    stop=int((i+1)*tau/dt)
    X_blocks.append(np.max(X_avg[start:stop]))

X_blocks.sort()

A=[]
T=[]
a=0
while a<=np.max(X_blocks):
    p=0
    for i in range(len(X_blocks)):
        if X_blocks[i]>=a:
            p=p+1

    A.append(a)
    T.append(-tau/log(1-p/len(X_blocks)))
    a=a+0.05

plt.plot(np.log10(T),A,marker="*",label="Direct sampling")

plt.xlabel("log10(return time)")
plt.ylabel("a")

#np.save('a_direct.npy', A)
#np.save('t_direct.npy', T)

plt.grid(True)
plt.legend()
plt.show()

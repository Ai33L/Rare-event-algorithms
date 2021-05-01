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

X = np.zeros(N)
X[0]=np.random.normal(0,sqrt(epsilon/alpha))

for j in range(N-1):
    X[j+1] = X[j] - alpha*X[j]*dt + sqrt(dt*2*epsilon)*np.random.normal(0,1)

np.save('series.npy', X)

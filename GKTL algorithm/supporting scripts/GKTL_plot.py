import numpy as np
import matplotlib.pyplot as plt
from math import *
import seaborn as sns


a_alg=np.load('a_alg.npy')
t_alg=np.load('t_alg.npy')

a_tams=np.load('A_TAMS.npy')
t_tams=np.load('T_TAMS.npy')

a_direct=np.load('a_direct.npy')
t_direct=np.load('t_direct.npy')

plt.plot(np.log10(t_direct),a_direct,marker="*",label="Direct sampling")
plt.plot(np.log10(t_alg),a_alg,label="GKTL algorithm")
#plt.plot(t_tams,a_tams,label="TAMS algorithm")

plt.xlabel("log10(r(a))")
plt.ylabel("a")
#plt.xlim([0,13])
#plt.ylim([0,0.9])

plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *

a_theory=np.load('a_theory.npy')
t_theory=np.load('t_theory.npy')

a_direct=np.load('a_direct.npy')
t_direct=np.load('t_direct.npy')

a=np.load('A.npy')
t1=np.load('T1.npy')
t2=np.load('T2.npy')
t3=np.load('T3.npy')
t4=np.load('T4.npy')
t5=np.load('T5.npy')
t6=np.load('T6.npy')
t7=np.load('T7.npy')
t8=np.load('T8.npy')
t9=np.load('T9.npy')
t10=np.load('T10.npy')


t=(t1+t2+t3+t4+t5+t6+t7+t8+t9+t10)/10

t_z=np.linspace(0.5,14.2, num=25)
da=[]
a_est=[]
for i in range(len(t_z)):
    val_arr=np.array([np.interp(t_z[i],t1,a),np.interp(t_z[i],t2,a),np.interp(t_z[i],t3,a),np.interp(t_z[i],t4,a),
                      np.interp(t_z[i],t5,a),np.interp(t_z[i],t6,a),np.interp(t_z[i],t7,a),np.interp(t_z[i],t8,a),
                     np.interp(t_z[i],t9,a),np.interp(t_z[i],t10,a)])
    da.append(np.std(val_arr))
    a_est.append(np.mean(val_arr))

#da=np.array(da)*2.262/sqrt(10)
da=np.array(da)*2.262

plt.xlabel("log10(r(a))")
plt.ylabel("a")
plt.xlim([0,14])
plt.ylim([1,6])
plt.fill_between(t_z,a_est-da,a_est+da,color="grey",alpha=0.3)
#plt.plot(t_theory,a_theory,linewidth=0.75,color="green",label="Theory")
#plt.plot(t_direct,a_direct,marker='*',label="Direct sampling")
#plt.plot(t_z,a_est,color="red",linewidth=0.75,label="TAMS algorithm")
plt.plot(t,a,color="red",linewidth=0.75,marker='+',label="TAMS algorithm")
plt.grid(True)
plt.legend()
plt.savefig('fig.png')

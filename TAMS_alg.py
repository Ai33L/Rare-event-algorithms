import numpy as np
import matplotlib.pyplot as plt
import math


"""
Setting constants that will be used later in the code.
alpha and epsilon are the parameters of the Ornstein Uhlenbeck process.
Ta is the trajectory timelength and dt is the timestep for the process.
Num_traj is the number of trajectories that we want to create.
"""
alpha=1
epsilon= 0.5
Ta=10
dt=1/10000
N=int(Ta/dt)
Num_traj=100


"""
This function mutates the given trajectory as per the algorithm.
Clones the passed trajectory till Qmin is reached for the first time, and then simulate the rest.
Returns the mutated trajectory.
"""
def Mutate(X,Qmin):
    Xnew=X.copy()
    switch=0
    for m in range(N):
        if switch==0 and Xnew[m]>Qmin:
            switch=1
        if switch==1 and m!=N-1:
            Xnew[m+1] = Xnew[m] - alpha*Xnew[m]*dt + math.sqrt(dt*2*epsilon)*np.random.normal(0,1)

    return Xnew


"""
This function is called at each algorithm iteration.
Takes the existing trajectories, finds the trajectory/trajectories with least Max_score and replaces them with mutated trajectories.
Returns the updated trajectory weights along with the Min_score value.
"""
def TAMS_iter(data,w):
    Max_score=[]

    for i in range(Num_traj):
        Max_score.append(max(data[i]))

    Min_score=min(Max_score)
    print(Min_score)

    flag=[]
    for i in range(Num_traj):
        if Min_score==Max_score[i]:
            flag.append(i)

    for fl in flag:
        while True:
            random_traj=np.random.randint(0,Num_traj-1)
            if random_traj not in flag:
                break

        data[fl]= Mutate(data[random_traj],Min_score)

    w=w*(1-len(flag)/Num_traj)
    return(Min_score,w)


"""
This function creates the required number initial trajectories and iterate the algorithm.
Returns two lists, list of 'a' values and corresponding return time values. These can be used to directly plot the results.
Number of data points returned can be changed by changing the stepper for a_value(see line 104).
the variable w is the weight associated with the trajectories, that has to be changed after each algorithm timestep.
"""
def Return_time(a_start,a_stop):

    a_value=a_start
    w=1
    data = []

    for i in range(Num_traj):
        X = np.zeros(N)
        X[0]=np.random.normal(0,math.sqrt(epsilon/alpha))

        for j in range(N):
            X[j] = X[j-1] - alpha*X[j-1]*dt + math.sqrt(dt*2*epsilon)*np.random.normal(0,1)

        data.append(X)

    A_values=[]
    T_values=[]

    """
    Usually, we would need to score the trajectories before and after each timestep.
    Maintaining a log of the value of time in the previous step makes the code more efficient and reduces runtime.
    """
    t_prev=0

    while a_value<=a_stop:
        a_min,w = TAMS_iter(data,w)
        t_curr=-Ta/math.log(1-w)
        if a_min>=a_value:
            A_values.append(a_value)
            T_values.append(t_prev)
            a_value=a_value+0.2
        t_prev=t_curr

    return(T_values,A_values)


T1,A = Return_time(1,5.8)
#np.save('A.npy', A)
#np.save('T1.npy', np.log10(T1))


plt.plot(np.log10(T1),A)
plt.grid(True)
plt.show()

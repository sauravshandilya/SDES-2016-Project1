from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def LotkaVolterra(state,t):
    number_of_prey = state[0]
    number_of_prediator = state[1]
    
    growth_rate_of_prey      = 0.1
    death_rate_of_prey       = 0.1
    death_rate_of_prediator  = 0.1
    growth_rate_of_prediator = 0.1
    
    rate_of_change_of_prey      = number_of_prey*(growth_rate_of_prey - death_rate_of_prey*number_of_prediator)
    rate_of_change_of_prediator = -number_of_prediator*(death_rate_of_prediator - growth_rate_of_prediator*number_of_prey)
    return [rate_of_change_of_prey,rate_of_change_of_prediator]

t = range(0,500,1)
state0 = [1,0.5]                             #initial condition 5 prey and 1 prediator
state = odeint(LotkaVolterra,state0,t)
plt.figure()
plt.plot(t,state)
#plt.ylim([0,8])
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend(('x (prey)','y (predator)'))
plt.title('Lotka-Volterra -Frequency Plot')
plt.show()

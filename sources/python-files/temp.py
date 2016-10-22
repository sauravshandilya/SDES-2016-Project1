import numpy as np 
import matplotlib.pyplot as plt


def derivative(State):
	# StateDot = np.asarray([0.0,0.0])
	# return StateDot

	m = 1.0
	k = 1.0
	c = 3.0
	ucontrol = 0.0

	# print m,c,k

	A = np.asarray([[0.0,1.0],[-k/m,-c/m]])
	B = np.array([0.0,1.0/m])

	# print "zeta",c/(2*np.sqrt(k*m))

	StateDot = np.dot(A,State)+B*ucontrol
	return StateDot

State = np.array([1.0,-2.0])
StateDot = derivative(State)

tinitial = 0.0
tfinal = 25 #int(value[4])	#type casted to int - if in case user gives float
timestep = 0.01	
time = np.arange(tinitial,tfinal+timestep,timestep)

StateOut = np.zeros((2,len(time)))


for idx in range(len(time)):
	# print "simulation",time[idx]/tfinal*100
	StateOut[:,idx] = State
	StateDot = derivative(State)
	State += StateDot*timestep

position = StateOut[0,:]
print position
plt.figure()
plt.plot(time,position)

plt.show()

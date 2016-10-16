import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

t = range(0,500,1)
state0 = [1,0.5]
global state


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(0, 2)
ax.set_xlim(0, 5)
ax.grid()
xdata, ydata_1, ydata_2 = [], [], []

plotlays, plotcols = [2], ["black","red"]
lines = []

for index in range(2):
    lobj = ax.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)

def LotkaVolterra(state,t):

	number_of_prey = state[0]
	number_of_prediator = state[1]

	growth_rate_of_prey      = 0.1
	death_rate_of_prey       = 0.1
	death_rate_of_prediator  = 0.1
	growth_rate_of_prediator = 0.1

	rate_of_change_of_prey      = number_of_prey*(growth_rate_of_prey - death_rate_of_prey*number_of_prediator)
	rate_of_change_of_prediator = -number_of_prediator*(death_rate_of_prediator - growth_rate_of_prediator*number_of_prey)
	return rate_of_change_of_prey, rate_of_change_of_prediator

state = odeint(LotkaVolterra,state0,t)

def data_gen():
	t_min = 0
	cnt = 0
	i = 0
	state0 = [1,0.5]
	while cnt < 1000:
		time = []
		state_1 = []
		i = (i%490)+1	
		cnt += 1	
		yield t[i],state[i][0],state[i][1]
		# print time,state_1
		
		
		# print t,state
		# t_min += 10


# 	t = data_gen.t
# 	cnt = 0
# 	while cnt < 1000:
# 		cnt+=1
# 		t += 0.05
# 		yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
# data_gen.t = 0


def update(data):
	x,y = [],[]
    # update the data
	t,state_1,state_2 = data
	# print t,state
	xdata.append(t)
	ydata_1.append(state_1)
	ydata_2.append(state_2)
	# print xdata,ydata_1,ydata_2
	xmin, xmax = ax.get_xlim()
	if t >= xmax:
		ax.set_xlim(xmin, 2*xmax)
		ax.figure.canvas.draw()
	x.append(xdata)
	y.append(ydata_1)	
	y.append(ydata_2)

	# for i in range(2):
	# 	line.set_data(x,y[i])
	# # line.set_data(xdata, ydata_2)

	for lnum,line in enumerate(lines):
		line.set_data(x, y[lnum])

	return lines

ani = animation.FuncAnimation(fig, update, data_gen, blit=True, interval=10,
    repeat=True)
plt.show()
# data_gen()
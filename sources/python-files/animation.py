import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import readcsv as rcf
import matplotlib 
matplotlib.use("Agg")

global position
global StateOut
global time

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


position = []
# time = list(np.arange(0.0,25+0.01,0.01))

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

def derivative(value,State):
	# StateDot = np.asarray([0.0,0.0])
	# return StateDot

	m = float(value[0])
	k = float(value[1])
	c = float(value[2])
	ucontrol = float(value[3])

	# print m,c,k

	A = np.asarray([[0.0,1.0],[-k/m,-c/m]])
	B = np.array([0.0,1.0/m])

	# print "zeta",c/(2*np.sqrt(k*m))

	StateDot = np.dot(A,State)+B*ucontrol
	return StateDot

def create_state_matrix(value):
	global multiple_plot_value
	# value = list(np.ones(len(get_data_precalculated[1][1:])))
	State = np.array([0.0,1.0])
	StateDot = derivative(value,State)
	
	tinitial = 0.0
	tfinal = 25#int(value[4])	#type casted to int - if in case user gives float
	timestep = 0.01

	time = np.arange(tinitial,tfinal+timestep,timestep)
	print "time", len(time)

	StateOut = np.zeros((2,len(time)))
	multiple_plot_value = np.zeros((2,len(time)))
	print "satetout", len(StateOut[0])	

	for idx in range(len(time)):
		# print "simulation",time[idx]/tfinal*100

		StateOut[:,idx] = State
		StateDot = derivative(value,State)
		State += StateDot*timestep

	# position = StateOut[0,:]
	return StateOut[0]

def response_plot(data):
	global time
	global multiple_plot_value
	global StateOut

	multiple_plot_value = []

	ylimit = []
	xlimit = []

	plot_title = "Dynamic Response of System"

	# plotting only three values
	for i in range (1,len(get_data_precalculated)-1):
		value = []
		for j in range (1,len(get_data_precalculated[i])):
			value.append(get_data_precalculated[i][j])

		tinitial = 0.0
		tfinal = 25 #int(value[4])	#type casted to int - if in case user gives float
		timestep = 0.01	
		time = np.arange(tinitial,tfinal+timestep,timestep)
		
		StateOut = create_state_matrix(value)
		# return StateOut[0]
		multiple_plot_value = StateOut[0]
	# return multiple_plot_value
get_data_precalculated = rcf.readcsvfile("precalculated_input_for_system_response_analysis.csv")		#readcsv_filename is filename defined at the top

position = response_plot(get_data_precalculated)
		# return position

def data_gen():
	global StateOut
	global multiple_plot_value
	global time

	t_min = 0
	cnt = 0
	i = 0
	# state0 = [1,0.5]
	while cnt < 2000:
		# time = []
		state_1 = []
		i = i+1	
		cnt += 1	
		yield time[i],StateOut[i]	
		


def update(data):
	x,y = [],[]
    # update the data
	time,state_1 = data
	# print time,state_1
	
	xdata.append(time)
	ydata_1.append(state_1)
	# ydata_2.append(state_2)
	# print xdata,ydata_1,ydata_2
	xmin, xmax = ax.get_xlim()
	ymin, ymax = ax.get_ylim()

	#change limit of axis, if max or min value has reached
	if time >= xmax:
		ax.set_xlim(xmin, 2*xmax)
		ax.figure.canvas.draw()
	if state_1 <= ymin:
		ax.set_ylim(state_1, ymax)
	if state_1 >= ymax:
		ax.set_ylim(ymin, state_1)

	x.append(xdata)
	y.append(ydata_1)	
	y.append(ydata_1)

	# for i in range(2):
	# 	line.set_data(x,y[i])
	# # line.set_data(xdata, ydata_2)
	ax.set_xlabel("Time (in sec)")
	ax.set_ylabel("Position")
	# ax.set_legend ("hi")
	for lnum,line in enumerate(lines):
		line.set_data(x, y[lnum])

	return lines

def init():
	for line in lines:
		line.set_data([],[])
	return lines

ani = animation.FuncAnimation(fig, update, data_gen, blit=True, interval=10,repeat=False,init_func=init)
# plt.show()

# ani.save('ani.mp4',fps=30,extra_args=['-vcodec','libx264'])

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
                                   blit=True)
im_ani.save('im.mp4', writer=writer)

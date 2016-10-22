#!/usr/bin/python

import numpy as np 
import matplotlib.pyplot as plt
import readcsv as rcf

folder_location = "../latex-files/images/"

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

def single_plotting (x_value,y_value,x_label,y_label,legend,figure_name,plot_name="Plot_Name.png",plot_title="Plot Title",linewidth=2.0,color='r',linestyle="-"):

	# tinitial = 0.0
	# tfinal = int(value[3])
	# timestep = 0.01

	# time = np.arange(tinitial,tfinal+timestep,timestep)

	# xthre = max(x_value)/len(x_value)
	# print "xthre",xthre

	plt.figure(figure_name)
	plt.plot(x_value,y_value,label=legend,linewidth=linewidth,color=color,linestyle=linestyle)
	# plt.plot(time,velocity,label='Velocity')
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.legend()
	plt.title(plot_title)
	# plt.ylim([min(y_value),max(y_value)])
	# plt.xlim([min(x_value)-(10*xthre),max(x_value)+(10*xthre)])
	# plt.xlim([min(x_value),max(x_value)])
	plt.grid()
	plt.savefig(folder_location+plot_name)
	# plt.savefig(plot_name)
	plt.show()


def create_state_matrix(value):
	# value = list(np.ones(len(get_data_precalculated[1][1:])))
	State = np.array([0.0,1.0])
	StateDot = derivative(value,State)
	
	tinitial = 0.0
	tfinal = 25#int(value[4])	#type casted to int - if in case user gives float
	timestep = 0.01

	time = np.arange(tinitial,tfinal+timestep,timestep)

	StateOut = np.zeros((2,len(time)))


	for idx in range(len(time)):
		# print "simulation",time[idx]/tfinal*100

		StateOut[:,idx] = State
		StateDot = derivative(value,State)
		State += StateDot*timestep

	# position = StateOut[0,:]
	return StateOut
	single_plotting(time,position,"Time (sec)","Position","Position","response") 
	# single_plotting(time,StateOut[1,:],"Time (sec)","Position","Position","response")

def response_plot(data):

	ylimit = []
	xlimit = []

	plot_title = "Dynamic Response of System"

	# plotting only three values
	for i in range (1,len(get_data_precalculated)-1):
		value = []
		for j in range (1,len(get_data_precalculated[i])):
			value.append(get_data_precalculated[i][j])

		# print value
		
		zeta = float(value[2])/(2*np.sqrt(float(value[0])*float(value[1])))
		legend = get_data_precalculated[i][0] + " Actual z= "+ str("{0:.2f}".format(zeta))

		tinitial = 0.0
		tfinal = 25 #int(value[4])	#type casted to int - if in case user gives float
		timestep = 0.01	
		time = np.arange(tinitial,tfinal+timestep,timestep)
		
		StateOut = create_state_matrix(value)
		position = StateOut[0,:]

		plt.figure("Response")
		
		plt.plot(time,position,label=legend,linewidth=2.0)
		plt.legend()
	
	plt.title(plot_title)
	plt.ylabel("Displacement")
	plt.xlabel("time(in sec)")

	plt.xlim([min(time),max(time)])
	plt.grid()
	# plt.show()
	plt.savefig(folder_location+"Response.png")


if __name__ == '__main__':
	get_data = []

	get_data_precalculated = rcf.readcsvfile("precalculated_input_for_system_response_analysis.csv")		#readcsv_filename is filename defined at the top

	precalculated_data_points = []

	value = []
	for i in range (1,len(get_data_precalculated[1])):
		value.append(get_data_precalculated[1][i])

	tinitial = 0.0
	tfinal = int(value[4])
	timestep = 0.01
	time = np.arange(tinitial,tfinal+timestep,timestep)

	response_plot(get_data_precalculated)

	value = []
	value = get_data_precalculated[4][1:]
	
	undamped = create_state_matrix(value)
	single_plotting(time,undamped[0,:],"Time (in sec)","Distance (in cm)","Undamped","Undamped response",plot_name="Undamped_Response.png",plot_title="Undamped Response",color="r",linestyle="--")



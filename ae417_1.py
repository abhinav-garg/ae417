import code
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.ion()
def calc_cg():
	'''
	Input: Height of human, wing chord, 
	Units: All SI
	'''
	# te_loc =  # To be evaluated
	# Given
	human_weight = 80
	root_chord = 0.55
	wing_weight = 15
	fuel_weight = 66
	engine_weight = 20
	num_engines = 2
	height = 1.7
	# CGs
	human_cg = 0.55*height
	# Wing CG at c/2 approximately
	wing_cg = root_chord/2.
	a_1, a_2 = np.mgrid[0:0.55:100*1j, 0:1.7:100*1j]
	total_cg = 1./(human_weight+wing_weight+fuel_weight) * (human_cg*human_weight + (a_2+root_chord-a_1)*num_engines*engine_weight + (a_2+root_chord/2.)*(wing_weight+fuel_weight))
	new_var = total_cg - (a_2+3.*root_chord/4.)
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(1,1,1, projection='3d')
	ax1.set_xlabel('CG of engine from leading edge'); ax1.set_ylabel('Trailing edge of wing from ground'); ax1.set_zlabel('Total vehicle CG')
	surf = ax1.plot_surface(a_1,a_2,total_cg)
	
	fig2 = plt.figure()
	ax2 = fig2.add_subplot(1,1,1, projection='3d')
	ax2.set_xlabel('CG of engine from leading edge'); ax2.set_ylabel('Trailing edge of wing from ground'); ax2.set_zlabel('')
	surf = ax2.plot_surface(a_1,a_2,new_var)
	
	plt.draw()
	code.interact(local=dict(globals(), **locals()))

calc_cg()
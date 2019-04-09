"""
 Middle East Technical University
 Computer Engineering
 2018 Fall
 CENG111 - Introduction to Computer Engineering Concepts
 THE3 - The Movement of Particules Issue
 
 ID: 2319143
 Full Name: Ersegun Omer EROL

 ALL RIGHTS RESERVED...

"""
from math import sqrt
from draw import *
from evaluator import *

def inner_sum(mass_set, position_set, which_particule):

	temp_sum_x = 0
	temp_sum_y = 0

	curr_x_sqr = 0
	curr_y_sqr = 0
	division_value = 0

	for i, j in enumerate(position_set):

		if not (i == which_particule - 1 or i == which_particule):

			if i % 2 == 0:
				curr_x_sqr = (j - position_set[which_particule - 1])**2

				x_will_be_incremented = False
				x_will_be_decremented = False

				if j > position_set[which_particule - 1]:
					x_will_be_incremented = True
				else:
					x_will_be_decremented = True

			elif i % 2 == 1:
				curr_y_sqr = (j - position_set[which_particule])**2
				division_value = mass_set[i] / (sqrt(curr_x_sqr + curr_y_sqr))**3

				y_will_be_incremented = False
				y_will_be_decremented = False

				if j > position_set[which_particule]:
					y_will_be_incremented = True
				else:
					y_will_be_decremented = True

				if x_will_be_incremented:
					temp_sum_x += division_value * abs(position_set[i - 1] - position_set[which_particule - 1])
				elif x_will_be_decremented:
					temp_sum_x -= division_value * abs(position_set[i - 1] - position_set[which_particule - 1])
				if y_will_be_incremented:
					temp_sum_y += division_value * abs(j - position_set[which_particule])
				elif y_will_be_decremented:
					temp_sum_y -= division_value * abs(j - position_set[which_particule])

				
	return [temp_sum_x, temp_sum_y]

my_data_set = []
my_data_set = get_data()

def new_move():

	global my_data_set

	G = my_data_set[0]	#gets the 'G' value
	dt = my_data_set[1]	#gets dt
	mass_set = []
	position_set = []
	new_position_set = []
	velocity_set = []
	f_sum_set = []
	result_list = []
	last_result_list = []
	number_of_particules = 0
	
	# Now we will get all masses, positions and velocities into the lists:
	for i in my_data_set:
		if type(i) == list:
			mass_set.append(my_data_set[my_data_set.index(i)][0])
			mass_set.append(my_data_set[my_data_set.index(i)][0])
			position_set.append(my_data_set[my_data_set.index(i)][1])
			position_set.append(my_data_set[my_data_set.index(i)][2])
			velocity_set.append(my_data_set[my_data_set.index(i)][3])
			velocity_set.append(my_data_set[my_data_set.index(i)][4])

	#print "mass_set", mass_set
	#print "1st position_set", position_set
	#print "1st velocity_set", velocity_set

	# After this step our lists will be like:
	#
	# mass_set = [m1, m1, m2, m2, m3, m3]
	# indicies....0...1...2...3...4....5
	#
	# position_set = [x01, y01, x02, y02, x03, y03]
	# indicies.........0....1....2....3....4....5
	#
	# velocity_set = [v0x1, v0y1, v0x2, v0y2, v0x3, v0y3]
	# indicies.........0.....1.....2.....3.....4.....5

	# Now we will calculate the number of particules:
	number_of_particules = len(mass_set) / 2

	# In ternms of "equation1"
	for i, j in enumerate(position_set):
		for k, l in enumerate(velocity_set):
			if i == k:
				new_position_set.append(j + float(dt * l))

	# After this step "new_position_set" will look like:
	# 
	# new_position_set = [x01, y01, x02, y02, x03, y03]
	# indicies.............0....1....2....3....4....5

	# In terms of "equation3",
	# Now we will calculate Fsums for each particule by the help of our helper function "inner_sum" and
	#will add them to the list f_sum_set consecutively:
	for i in range(1, len(mass_set), 2):
		one_time_use = inner_sum(mass_set, new_position_set, i)
		f_sum_set.append(G * mass_set[i - 1] * one_time_use[0])
		f_sum_set.append(G * mass_set[i - 1] * one_time_use[1])

	# After this step f_sum_set will look like:
	# 
	# f_sum_set = [Fx1, Fy1, Fx2, Fy2, Fx3, Fy3]
	# indicies......0....1....2....3....4....5

	# In terms of "equation2",
	# Now we will update all velocities:
	for i, j in enumerate(velocity_set):
		for k, l in enumerate(f_sum_set):
			if i == k:
				velocity_set[i] = j + dt * float(l / mass_set[i])

	# Now we will calculate the difference between positions and append them to our list "result_list"		
	for i, j in enumerate(position_set):
		for k, l in enumerate(new_position_set):
			if i == k:
				result_list.append(l - j)

	# We will reform our "result_list" to be able to return it in the correct form as "last_result_list"
	for i, j in enumerate(result_list):
		if i % 2 == 1:
			last_result_list.append([result_list[i-1], result_list[i]])

	# Reassigning the updated values to "my_data_set:"
	k = 2

	for i in range(0, len(new_position_set), 2):
		my_data_set[k][1] = new_position_set[i]
		k += 1

	k = 2

	for i in range(1, len(new_position_set), 2):
		my_data_set[k][2] = new_position_set[i]
		k += 1

	k = 2

	for i in range(0, len(velocity_set), 2):
		my_data_set[k][3] = velocity_set[i]
		k += 1

	k = 2

	for i in range(1, len(velocity_set), 2):
		my_data_set[k][4] = velocity_set[i]
		k += 1

	#print last_result_list
	return last_result_list

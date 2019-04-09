"""
 Middle East Technical University
 Computer Engineering
 2018 Fall
 CENG111 - Introduction to Computer Engineering Concepts
 THE2 - The Firmus Issue
 
 ID: 2319143
 Full Name: Ersegun Omer EROL

 ALL RIGHTS RESERVED...

"""
def is_firmus(ds1,ds2):
	#ds stands for "diagonal_set"

	#lets create a firmus_checklist
	firmus_checklist = []

	#our epsilon value
	epsilon = 0.001
	
	#After assigining the corners will be as following:
	# (x4,y4)	(x3,y3)
	#    -----------
	#    |         |
	#    | our     |
	#    |   block |
	#    |         |
	#    -----------
	# (x1,y1)	(x2,y2)

	#Firtsly lets assign ds1's all corners
	#	according to the given positions as block 'alfa'

	if (ds1[0] < ds1[2]) and (ds1[1] > ds1[3]):
		#then the given corners are sequentially
		#upper-left & lower-right
		alfa_x1 = ds1[0]
		alfa_y1 = ds1[3]
		alfa_x2 = ds1[2]
		alfa_y2 = ds1[3]
		alfa_x3 = ds1[2]
		alfa_y3 = ds1[1]
		alfa_x4 = ds1[0]
		alfa_y4 = ds1[1]

	elif (ds1[0] < ds1[2]) and (ds1[1] < ds1[3]):
		#then the given corners are sequentially
		#lower-left & upper-right
		alfa_x1 = ds1[0]
		alfa_y1 = ds1[1]
		alfa_x2 = ds1[2]
		alfa_y2 = ds1[1]
		alfa_x3 = ds1[2]
		alfa_y3 = ds1[3]
		alfa_x4 = ds1[0]
		alfa_y4 = ds1[3]

	elif (ds1[0] > ds1[2]) and (ds1[1] < ds1[3]):
		#then the given corners are sequentially
		#lower-right & upper-left
		alfa_x1 = ds1[2]
		alfa_y1 = ds1[1]
		alfa_x2 = ds1[0]
		alfa_y2 = ds1[1]
		alfa_x3 = ds1[0]
		alfa_y3 = ds1[3]
		alfa_x4 = ds1[2]
		alfa_y4 = ds1[3]

	else: #(ds1[0] > ds1[2]) and (ds1[1] > ds1[3]):
		#then the given corners are sequentially
		#upper-right & lower left
		alfa_x1 = ds1[2]
		alfa_y1 = ds1[3]
		alfa_x2 = ds1[0]
		alfa_y2 = ds1[3]
		alfa_x3 = ds1[0]
		alfa_y3 = ds1[1]
		alfa_x4 = ds1[2]
		alfa_y4 = ds1[1]

	#Secondly lets assign ds2's all corners
	#	according to the given positions as block 'beta'

	if (ds2[0] < ds2[2]) and (ds2[1] > ds2[3]):
		#then the given corners are sequentially
		#upper-left & lower-right
		beta_x1 = ds2[0]
		beta_y1 = ds2[3]
		beta_x2 = ds2[2]
		beta_y2 = ds2[3]
		beta_x3 = ds2[2]
		beta_y3 = ds2[1]
		beta_x4 = ds2[0]
		beta_y4 = ds2[1]

	elif (ds2[0] < ds2[2]) and (ds2[1] < ds2[3]):
		#then the given corners are sequentially
		#lower-left & upper-right
		beta_x1 = ds2[0]
		beta_y1 = ds2[1]
		beta_x2 = ds2[2]
		beta_y2 = ds2[1]
		beta_x3 = ds2[2]
		beta_y3 = ds2[3]
		beta_x4 = ds2[0]
		beta_y4 = ds2[3]

	elif (ds2[0] > ds2[2]) and (ds2[1] < ds2[3]):
		#then the given corners are sequentially
		#lower-right & upper-left
		beta_x1 = ds2[2]
		beta_y1 = ds2[1]
		beta_x2 = ds2[0]
		beta_y2 = ds2[1]
		beta_x3 = ds2[0]
		beta_y3 = ds2[3]
		beta_x4 = ds2[2]
		beta_y4 = ds2[3]

	else: #(ds2[0] > ds2[2]) and (ds2[1] > ds2[3]):
		#then the given corners are sequentially
		#upper-right & lower left
		beta_x1 = ds2[2]
		beta_y1 = ds2[3]
		beta_x2 = ds2[0]
		beta_y2 = ds2[3]
		beta_x3 = ds2[0]
		beta_y3 = ds2[1]
		beta_x4 = ds2[2]
		beta_y4 = ds2[1]

	#Lets calculate their mass abscissas:
	ma_of_alfa_x = float(alfa_x1 + alfa_x2)/2.0
	ma_of_alfa_y = float(alfa_y1 + alfa_y3)/2.0

	ma_of_beta_x = float(beta_x1 + beta_x2)/2.0
	ma_of_beta_y = float(beta_y1 + beta_y3)/2.0

	#Now lets define the blocks' places according to
	#	their mass abscissa and check the rules
	if ma_of_alfa_y > ma_of_beta_y:
		#alfa is at a higher position than beta

		#It's our rules' turn to go
		#Rule-1:The lower block should have its lower edge
		#		placed directly on the x axis
		if abs(beta_y1) < epsilon:
			#Rule-1 has passed
			firmus_checklist.append(1)
		else:
			#Rule-1 has failed
			firmus_checklist.append(0)

		#Rule-2:The upper block should have its lower edge
		#		(at least partically) coincide with the upper
		#		edge of the lower block
		if abs(alfa_y1 - beta_y4) < epsilon:
			#if ((alfa_x1 <= beta_x4 <= alfa_x2) or (alfa_x1 <= beta_x3 <= alfa_x2) or ((beta_x4 < alfa_x1 < beta_x3) and (beta_x4 < alfa_x2 < beta_x3))):
			if (alfa_x1 < beta_x4 < alfa_x2) or (abs(alfa_x1 - beta_x4) < epsilon) or (abs(beta_x4 - alfa_x2) < epsilon) or (alfa_x1 < beta_x3 < alfa_x2) or (abs(alfa_x1 - beta_x3) < epsilon) or (abs(beta_x3 - alfa_x2) < epsilon) or ((beta_x4 < alfa_x1 < beta_x3) and (beta_x4 < alfa_x2 < beta_x3)) or ((beta_x4 < alfa_x1) and (beta_x3 > alfa_x4)):
				#Rule-2 has passed
				firmus_checklist.append(1)
			else:
				#Rule-2 has failed
				firmus_checklist.append(0)
		else:
			#Rule-2 has failed
			firmus_checklist.append(0)

		#Rule-3:The upper block should have its center of mass
		#		abscissa in the range of the lower block's
		#		upper edge
		if beta_x4 < ma_of_alfa_x < beta_x3:
			#Rule-3 has passed
			firmus_checklist.append(1)
		elif (abs(ma_of_alfa_x - beta_x4) < epsilon) or (abs(ma_of_alfa_x - beta_x3) < epsilon):
			#Rule-3 has passed with consideration of epsilon value (stable/unstable issue on the2.pdf notes)
			firmus_checklist.append(1)
		else:
			#Rule-3 has failed
			firmus_checklist.append(0)
	
	else:
		#beta is at a higher position than alfa

		#It's our rules' turn to go
		#Rule-1:The lower block should have its lower edge
		#		placed directly on the x axis
		if abs(alfa_y1) < epsilon:
			#Rule-1 has passed
			firmus_checklist.append(1)
		else:
			#Rule-1 has failed
			firmus_checklist.append(0)

		#Rule-2:The upper block should have its lower edge
		#		(at least partically) coincide with the upper
		#		edge of the lower block
		if (abs(beta_y1 - alfa_y4) < epsilon):
			#if ((beta_x1 <= alfa_x4 <= beta_x2) or (beta_x1 <= alfa_x3 <= beta_x2) or ((alfa_x4 < beta_x1 < alfa_x3) and (alfa_x4 < beta_x2 < alfa_x3))):
			if (beta_x1 < alfa_x4 < beta_x2) or (abs(beta_x1 - alfa_x4) < epsilon) or (abs(alfa_x4 - beta_x2) < epsilon) or (beta_x1 < alfa_x3 < beta_x2) or (abs(beta_x1 - alfa_x3) < epsilon) or (abs(alfa_x3 - beta_x2) < epsilon) or ((alfa_x4 < beta_x1 < alfa_x3) and (alfa_x4 < beta_x2 < alfa_x3)) or ((alfa_x4 < beta_x1) and (alfa_x3 > beta_x4)):
				#Rule-2 has passed
				firmus_checklist.append(1)
			else:
				#Rule-2 has failed
				firmus_checklist.append(0)
		else:
			#Rule-2 has failed
			firmus_checklist.append(0)
		
		#Rule-3:The upper block should have its center of mass
		#		abscissa in the range of the lower block's
		#		upper edge
		if (alfa_x4 < ma_of_beta_x < alfa_x3):
			#Rule-3 has passed
			firmus_checklist.append(1)
		elif (abs(ma_of_beta_x - alfa_x4) < epsilon) or (abs(ma_of_beta_x - alfa_x3) < epsilon):
			#Rule-3 has passed with consideration of epsilon value (stable/unstable issue on the2.pdf notes)
			firmus_checklist.append(1)
		else:
			#Rule-3 has failed
			firmus_checklist.append(0)

	#It's time to define the type of the blocks
	if firmus_checklist == [1,1,1]:
		#is firmus
		area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
		return ["FIRMUS",float(area)]
	elif firmus_checklist == [1,1,0]:
		if ma_of_alfa_y > ma_of_beta_y:
			#alfa is on beta
			if ma_of_alfa_x < ma_of_beta_x:
				#teta must be added to right
				teta_x2 = 2*beta_x4 - alfa_x1
				teta_y2 = alfa_y2
				teta_x1 = alfa_x2
				teta_y1 = alfa_y1
				teta_x3 = teta_x2
				teta_y3 = alfa_y3
				teta_x4 = alfa_x2
				teta_y4 = alfa_y4
				teta = [teta_x1, teta_y1, teta_x3, teta_y3]
				return ["ADDENDUM",teta]
			else:
				#teta must be added to left
				teta_x1 = 2*beta_x3 - alfa_x2
				teta_y1 = alfa_y1
				teta_x2 = alfa_x1
				teta_y2 = alfa_y2
				teta_x3 = alfa_x4
				teta_y3 = alfa_y3
				teta_x4 = teta_x1
				teta_y4 = alfa_y4
				teta = [teta_x1, teta_y1, teta_x3, teta_y3]
				return ["ADDENDUM",teta]
		else:
			#beta is on alfa
			if ma_of_beta_x < ma_of_alfa_x:
				#teta must be added to right
				teta_x2 = 2*alfa_x4 - beta_x1
				teta_y2 = beta_y2
				teta_x1 = beta_x2
				teta_y1 = beta_y1
				teta_x3 = teta_x2
				teta_y3 = beta_y3
				teta_x4 = beta_x2
				teta_y4 = beta_y4
				teta = [teta_x1, teta_y1, teta_x3, teta_y3]
				return ["ADDENDUM",teta]
			else:
				#teta must be added to left
				teta_x1 = 2*alfa_x3 - beta_x2
				teta_y1 = beta_y1
				teta_x2 = beta_x1
				teta_y2 = beta_y2
				teta_x3 = beta_x4
				teta_y3 = beta_y3
				teta_x4 = teta_x1
				teta_y4 = beta_y4
				teta = [teta_x1, teta_y1, teta_x3, teta_y3]
				return ["ADDENDUM",teta]
	else:
		#is damnare
		if (alfa_x1 < beta_x4 < alfa_x2) and (alfa_y1 < beta_y4 < alfa_y4) and not (alfa_x1 < beta_x3 < alfa_x2) and (alfa_y1 < beta_y3 < alfa_y4) and not (alfa_x1 < beta_x2 < alfa_x2) and not (alfa_y1 < beta_y2 < alfa_y4) and (alfa_x1 < beta_x1 < alfa_x2) and not (alfa_y1 < beta_y1 < alfa_y4):
			#the overlapping position is like
			#    -----------
			#    | alfa    |
			#    |         |
			#    |     ----|------
			#    |     |   |     |
			#    -----------     |
			#		   |		 |
			#		   |    beta |
			#		   -----------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (beta_x1 < alfa_x4 < beta_x2) and (beta_y1 < alfa_y4 < beta_y4) and not (beta_x1 < alfa_x3 < beta_x2) and (beta_y1 < alfa_y3 < beta_y4) and not (beta_x1 < alfa_x2 < beta_x2) and not (beta_y1 < alfa_y2 < beta_y4) and (beta_x1 < alfa_x1 < beta_x2) and not (beta_y1 < alfa_y1 < beta_y4):
			#the overlapping position is like
			#    -----------
			#    | beta    |
			#    |         |
			#    |     ----|------
			#    |     |   |     |
			#    -----------     |
			#		   |		 |
			#		   |    alfa |
			#		   -----------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (alfa_x1 < beta_x3 < alfa_x2) and (alfa_y1 < beta_y3 < alfa_y4) and not (alfa_x1 < beta_x4 < alfa_x2) and (alfa_y1 < beta_y4 < alfa_y4) and not (alfa_x1 < beta_x1 < alfa_x2) and not (alfa_y1 < beta_y1 < alfa_y4) and (alfa_x1 < beta_x2 < alfa_x2) and not (alfa_y1 < beta_y2 < alfa_y4):
			#the overlapping position is like
			#		  -----------
			#		  |    alfa |
			#		  |			|
			#	------|----		|
			#	|	  |	  |		|
			#	|	  -----------
			#	|		  |
			#	| beta    |
			#	-----------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (beta_x1 < alfa_x3 < beta_x2) and (beta_y1 < alfa_y3 < beta_y4) and not (beta_x1 < alfa_x4 < beta_x2) and (beta_y1 < alfa_y4 < beta_y4) and not (beta_x1 < alfa_x1 < beta_x2) and not (beta_y1 < alfa_y1 < beta_y4) and (beta_x1 < alfa_x2 < beta_x2) and not (beta_y1 < alfa_y2 < beta_y4):
			#the overlapping position is like
			#		  -----------
			#		  |    beta |
			#		  |			|
			#	------|----		|
			#	|	  |	  |		|
			#	|	  -----------
			#	|		  |
			#	| alfa    |
			#	-----------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (alfa_x1 < beta_x4 < alfa_x2) and (alfa_y1 < beta_y4 < alfa_y4) and (alfa_x1 < beta_x3 < alfa_x2) and (alfa_y1 < beta_y3 < alfa_y4) and (alfa_x1 < beta_x2 < alfa_x2) and (alfa_y1 < beta_y2 < alfa_y4) and (alfa_x1 < beta_x1 < alfa_x2) and (alfa_y1 < beta_y1 < alfa_y4):
			#the overlapping position is like
			#	-----------------
			#	| alfa			|
			#	|				|
			#	|  	---------   |
			#	|	| beta	|	|
			#	|	|		|	|
			#	|	|	    |	|
			#	|	---------	|
			#	-----------------
			area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1)
			return ["DAMNARE",float(area)]
		elif (beta_x1 < alfa_x4 < beta_x2) and (beta_y1 < alfa_y4 < beta_y4) and (beta_x1 < alfa_x3 < beta_x2) and (beta_y1 < alfa_y3 < beta_y4) and (beta_x1 < alfa_x2 < beta_x2) and (beta_y1 < alfa_y2 < beta_y4) and (beta_x1 < alfa_x1 < beta_x2) and (beta_y1 < alfa_y1 < beta_y4):
			#the overlapping position is like
			#	-----------------
			#	| beta			|
			#	|  	---------   |
			#	|	| alfa	|	|
			#	|	|		|	|
			#	|	|	    |	|
			#	|	---------	|
			#	|				|
			#	|				|
			#	-----------------
			area = (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			return ["DAMNARE",float(area)]
		elif (alfa_x1 < beta_x4 < alfa_x2) and (alfa_y1 < beta_y4 < alfa_y4) and (alfa_x1 < beta_x3 < alfa_x2) and (alfa_y1 < beta_y3 < alfa_y4) and (alfa_x1 < beta_x2 < alfa_x2) and not (alfa_y1 < beta_y2 < alfa_y4) and (alfa_x1 < beta_x1 < alfa_x2) and not (alfa_y1 < beta_y1 < alfa_y4):
			#the overlapping position is like
			#	-----------------
			#	| alfa			|
			#	|  	---------   |
			#	|	| 		|	|
			#	----|-------|---|
			#		|  beta |	
			#		---------	
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (beta_x1 < alfa_x4 < beta_x2) and (beta_y1 < alfa_y4 < beta_y4) and (beta_x1 < alfa_x3 < beta_x2) and (beta_y1 < alfa_y3 < beta_y4) and (beta_x1 < alfa_x2 < beta_x2) and not (beta_y1 < alfa_y2 < beta_y4) and (beta_x1 < alfa_x1 < beta_x2) and not (beta_y1 < alfa_y1 < beta_y4):
			#the overlapping position is like
			#	-----------------
			#	| beta			|
			#	|  	---------   |
			#	|	| 		|	|
			#	----|-------|---|
			#		|  alfa |	
			#		---------	
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (beta_x1 < alfa_x4 < beta_x2) and not (beta_y1 < alfa_y4 < beta_y4) and (beta_x1 < alfa_x3 < beta_x2) and not (beta_y1 < alfa_y3 < beta_y4) and (beta_x1 < alfa_x2 < beta_x2) and (beta_y1 < alfa_y2 < beta_y4) and (beta_x1 < alfa_x1 < beta_x2) and (beta_y1 < alfa_y1 < beta_y4):
			#the overlapping position is like			
			#	  	---------   
			#		| alfa	|	
			#	----|-------|----
			#	|	|  		|	|
			#	|	---------	|
			#	|		   beta |
			#	-----------------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (alfa_x1 < beta_x4 < alfa_x2) and not (alfa_y1 < beta_y4 < alfa_y4) and (alfa_x1 < beta_x3 < alfa_x2) and not (alfa_y1 < beta_y3 < alfa_y4) and (alfa_x1 < beta_x2 < alfa_x2) and (alfa_y1 < beta_y2 < alfa_y4) and (alfa_x1 < beta_x1 < alfa_x2) and (alfa_y1 < beta_y1 < alfa_y4):
			#the overlapping position is like			
			#	  	---------   
			#		| beta	|	
			#	----|-------|----
			#	|	|  		|	|
			#	|	---------	|
			#	|		   alfa |
			#	-----------------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (alfa_x1 < beta_x4 < alfa_x2) and (alfa_y1 < beta_y4 < alfa_y4) and not (alfa_x1 < beta_x3 < alfa_x2) and (alfa_y1 < beta_y3 < alfa_y4) and not (alfa_x1 < beta_x2 < alfa_x2) and (alfa_y1 < beta_y2 < alfa_y4) and (alfa_x1 < beta_x1 < alfa_x2) and (alfa_y1 < beta_y1 < alfa_y4):
			#the overlapping position is like			
			#	-----------------
			#	| alfa			|
			#	|			----|-------
			#	|			|	|	   |
			#	|			|	| beta |
			#	|			----|-------
			#	-----------------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (beta_x1 < alfa_x4 < beta_x2) and (beta_y1 < alfa_y4 < beta_y4) and not (beta_x1 < alfa_x3 < beta_x2) and (beta_y1 < alfa_y3 < beta_y4) and not (beta_x1 < alfa_x2 < beta_x2) and (beta_y1 < alfa_y2 < beta_y4) and (beta_x1 < alfa_x1 < beta_x2) and (beta_y1 < alfa_y1 < beta_y4):
			#the overlapping position is like			
			#	-----------------
			#	| beta			|
			#	|			----|-------
			#	|			|	|	   |
			#	|			|	| alfa |
			#	|			----|-------
			#	|				|
			#	|				|
			#	-----------------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif not (alfa_x1 < beta_x4 < alfa_x2) and (alfa_y1 < beta_y4 < alfa_y4) and (alfa_x1 < beta_x3 < alfa_x2) and (alfa_y1 < beta_y3 < alfa_y4) and (alfa_x1 < beta_x2 < alfa_x2) and (alfa_y1 < beta_y2 < alfa_y4) and not (alfa_x1 < beta_x1 < alfa_x2) and (alfa_y1 < beta_y1 < alfa_y4):
			#the overlapping position is like			
			#			-----------------
			#			| alfa			|
			#	--------|----			|
			#	|		|	|			|
			#	| beta	|	|			|
			#	--------|----			|
			#			-----------------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif not (beta_x1 < alfa_x4 < beta_x2) and (beta_y1 < alfa_y4 < beta_y4) and (beta_x1 < alfa_x3 < beta_x2) and (beta_y1 < alfa_y3 < beta_y4) and (beta_x1 < alfa_x2 < beta_x2) and (beta_y1 < alfa_y2 < beta_y4) and not (beta_x1 < alfa_x1 < beta_x2) and (beta_y1 < alfa_y1 < beta_y4):
			#the overlapping position is like			
			#			-----------------
			#			| beta			|
			#	--------|----			|
			#	|		|	|			|
			#	| alfa	|	|			|
			#	--------|----			|
			#			|				|
			#			|				|
			#			-----------------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (beta_x1 < alfa_x4 < beta_x2) and not (beta_y1 < alfa_y4 < beta_y4) and (beta_x1 < alfa_x3 < beta_x2) and not (beta_y1 < alfa_y3 < beta_y4) and (beta_x1 < alfa_x2 < beta_x2) and not (beta_y1 < alfa_y2 < beta_y4) and (beta_x1 < alfa_x1 < beta_x2) and not (beta_y1 < alfa_y1 < beta_y4) and (beta_y4 < alfa_y4) and (alfa_y1 < beta_y1):
			#the overlapping position is like
			#	   		---------
			#	   		| alfa  |
			#			|		|
			#			|		|
			#	---------------------
			#	|  		|	    |  	|
			#	|  		|		|  	|
			#	| beta 	|		|	|
			#	---------------------
			#			|		|	
			#			---------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (alfa_x1 < beta_x4 < alfa_x2) and not (alfa_y1 < beta_y4 < alfa_y4) and (alfa_x1 < beta_x3 < alfa_x2) and not (alfa_y1 < beta_y3 < alfa_y4) and (alfa_x1 < beta_x2 < alfa_x2) and not (alfa_y1 < beta_y2 < alfa_y4) and (alfa_x1 < beta_x1 < alfa_x2) and not (alfa_y1 < beta_y1 < alfa_y4) and (alfa_y4 < beta_y4) and (beta_y1 < alfa_y1):
			#the overlapping position is like
			#	   		---------
			#	   		| beta  |
			#	---------------------
			#	|  		|	    |  	|
			#	|  		|		|  	|
			#	| alfa 	|		|	|
			#	---------------------
			#			|		|
			#			|		|
			#			|		|	
			#			---------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		elif (alfa_x2 == beta_x2) or (alfa_x4 == beta_x4) or (alfa_y4 == beta_y4) or (alfa_y1 == beta_y1):
			#any left, right, top or down lines are overlapping
			#for example:
			#	---------------------
			# 	|		|			|
			#	|		|			|
			#	|--------			|
			#	|					|
			#	---------------------
			total_area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			overlapping_area = (min(alfa_x2,beta_x2) - max(alfa_x1,beta_x1)) * (min(alfa_y4,beta_y4) - max(alfa_y2,beta_y2))
			area = total_area - overlapping_area
			return ["DAMNARE",float(area)]
		else:
			#no overlapping
			area = (alfa_x2 - alfa_x1) * (alfa_y4 - alfa_y1) + (beta_x2 - beta_x1) * (beta_y4 - beta_y1)
			return ["DAMNARE",float(area)]
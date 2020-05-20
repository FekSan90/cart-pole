import numpy as np

# obsLog contains the observation log, nn defines the number of neurons in the NN project
def evalSim(obsLog,nn = 0):
	obsSize = np.shape(obsLog)
	iterations = obsSize[0]
	time = iterations*0.02
	timeVec = np.arange(0,time,iterations)
	num_obs = obsSize[1]
	points = 0
	if num_obs != 4:
		print("Error: Observation array size mismatch! Must be 4 elements in a row.")
		return
	if iterations != 250:
		print("Error: Wrong number of iterations! Must be 250 - 5sec")
		return
	positions = obsLog[:,0]
	velocities = obsLog[:,1]
	angles = obsLog[:,2]*(180/np.pi)
	dangles = obsLog[:,3]*(180/np.pi)
	tasks = [15,15,10,10]
	successful = -1
	weight = np.zeros(4)
# Task 1
	score = 0
	for i in range(200):
		if(np.absolute(angles[i]) < 45):
			score += 1
	for i in range(200,250):
		if(angles[i] < 1 or angles[i] > -1):
			score += 1
	print("Score on task 1: ", score, "/250")
	if score == 250:
		successful = 0
		weight[0] = 1
# Task 2
	if successful == 0:
		score = 0
		for i in range(250):
			if(i >= 200 and np.absolute(angles[i]) < 1 and np.absolute(positions[i]) < 0.5 ):
				score += 1
			elif(i >= 150 and np.absolute(angles[i]) < 1 and np.absolute(positions[i]) < 0.5 ):
				weight[1] += 1
		print("Score on task 2: ", score, "/50")
		if score == 50:
			successful = 1
			weight[1] = weight[1]/50
# Task 3
	if successful == 1:
		score = 0
		for i in range(250):
			if(i >= 150 and np.absolute(angles[i]) < 0.5 and np.absolute(positions[i]) < 0.25 ):
				score += 1
			if(nn > 0):
				weight[2] = 1 - ((nn-10)/90)
			else:
				if i >= 150 and np.absolute(velocities[i]) <= 0.5:
					weight[2] += 1
		print("Score on task 3: ", score, "/100")
		if score == 100:
			successful = 2
			if nn == 0:
				weight[2] = weight[2]/100
# Task 4
	if successful == 2:
		score = 0
		for i in range(250):
			if(i >= 150 and np.absolute(angles[i]) < 0.1 and np.absolute(positions[i]) < 0.1 ):
				score += 1
			if(nn > 0):
				weight[3] = 1
			else:
				if i >= 150 and np.absolute(velocities[i]) <= 0.1:
					weight[3] += 1
		print("Score on task 4: ", score, "/100")
		if score == 100:
			successful = 3
			if nn == 0:
				weight[3] = weight[3]/100
	if successful >= 0:
		for i in range(successful+1):
			points += weight[i] * tasks[i]
	print("The number of points scored:", points)
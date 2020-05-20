import gym
import numpy as np
import math
from simple_pid import PID 
import matplotlib.pyplot as plt
# neptun kod alapjan
import YZ2ZBA as control
import tensorflow as tf
from tensorflow import keras
import h5py
import eval_sim
#-------------------
import time
def pend(pars,simulation_time,save):
	env = gym.make('CartPole-v0')
	observation = env.reset() # reset the simulation environment
	log_err_angle = np.zeros(simulation_time) # log the error signal
	log_err_pos = np.zeros(simulation_time) # log the error signal
	abs_force_sum = 0
	if save:
		inlog=[observation]
		outlog=[0]
	fitness = 0
	# ControllerType, type: -1,0,1 <= dPID,Fuzzy,NN
	#control.ControllerObj(type,pars)
	#control.ControllerObj() - default !FINAL! parameters, modify in <neptun>.py
	Controller = control.ControllerObj(-1,pars)
	# main loop
	obsLog = np.ones((simulation_time,4))
	for t in range(simulation_time):
		obsLog[t,:] = observation
		#env.render() # render the simulation
		cartpos = observation[0] # position of the cart
		angle = observation[2]*(180/np.pi) # angle of the pole
		log_err_angle[t] = np.absolute(0 - angle)*(t/simulation_time); # log the angle error (0 is the setpoint)
		log_err_pos[t] = np.absolute(0 - cartpos)*(t/simulation_time); # log the position error (0 is the setpoint)
		force = Controller.calculate(observation)
		if save:
			inlog=np.append(inlog, [observation], axis=0)
			outlog=np.append(outlog, [force], axis=0)
		
		abs_force_sum += np.absolute(force)*(t/simulation_time)
		observation, reward, done, info = env.step(force) # do the action, get the measurements
		if done and np.absolute(observation[2]*(180/np.pi)) > 45:
			fitness += 100000
			break
	abs_log_err_angle = np.absolute(log_err_angle)
	abs_log_err_pos = np.absolute(log_err_pos)
	abs_error_sum = np.sum(abs_log_err_angle) + np.sum(abs_log_err_pos)*10.0
	if save:
		plt.plot(log_err_angle[1:t])
		plt.show()
		plt.plot(log_err_pos[1:t])
		plt.show()
		np.savetxt("inlog.csv", inlog, delimiter=",")
		np.savetxt("outlog.csv", outlog, delimiter=",")
		eval_sim.evalSim(obsLog)
	env.close()
	# fitness function
	# abs_force_sum is optional
	fitness += abs_error_sum #+ abs_force_sum
	return fitness
	
	
	
	
	
	
	
	
	
	
	

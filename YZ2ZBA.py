import gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
import h5py
from skfuzzy import control as ctrl
#----------------------------
from simple_pid import PID 
#----------------------------

class ControllerObj:
	ControllerType = 1 # -1 PID, 0 Fuzzy, 1 Neural Network
# variables -----------
	pid_angle = None
	pid_pos = None
	loaded_model = None
	neurons = 9
# OWN variables HERE

	angle = 0.1
#-------------------
# Modify type! -1 PID, 0 Fuzzy, 1 Neural Network !!!!!!!!!
# pars default will be the final solution!!!!!!!!!!!!!!!!!

 
	def __init__(self, type = 1 ,pars = [-0.5614032 ,0.01 ,-2.9274734 ,-0.61085835 ,0.09279504, -9.01882262]):
		if type == -1:
			print("Warning: Using the default PID controller!")
			self.ControllerType = type
		elif type == 0 or type == 1 :
			self.ControllerType = type
		else:
			print("ControllerType is not in range! (-1,1)")
		if self.ControllerType == 0:
			configFuzzy(self,pars)
		elif self.ControllerType == 1:
			configNN(self,pars)
		elif self.ControllerType == -1:
			configdPID(self,pars)
		else:
			print("ControllerType is not in range! (-1,1)")
#--------------------------
	def getController(self):
		return self
#--------------------------
	def getControllerType(self):
		return self.ControllerType
#--------------------------
	def calculate(self,observation):
		if self.ControllerType == 0:
			# ------ Fuzzy controller --
			# Modify HERE
			# Example: force = self.fuzzCtrl.compute(observation)
			force = -1
			# If using Fuzzy delete this row:
			print("Fuzzy ControllerType not implemented!")
			return force
		elif self.ControllerType == 1:
			# ------ NN controller --
			y=self.loaded_model.predict(np.array([observation]))
			return y[0][0]
		elif self.ControllerType == -1:
			# ------ dPID controller --
			cartPos, cartVel, angle, angleVel = observation
			force_angle = self.pid_angle(angle*(180/np.pi));
			force_pos = self.pid_pos(cartPos);
			return force_angle + force_pos
		else:
			print("ControllerType is not in range! (-1,1)")

def configdPID(self,pars):
	# ------ dPID controller --
	setangle = 0.0;
	setpos = 0.0;
	self.pid_angle = PID(pars[0], pars[1], pars[2], setangle)
	self.pid_pos = PID(pars[3], pars[4], pars[5], setpos)
	self.pid_angle.sample_time = 0.02
	self.pid_pos.sample_time = 0.02

def configFuzzy(self,pars):
	# ------ Fuzzy controller --
	# include genFuzz(pars) here!
	# fuzzRuleCtrl = ctrl.ControlSystem(rules)
	# fuzzCtrl = ctrl.ControlSystemSimulation(fuzzRuleCtrl)
	self.fuzzCtrl = fuzzCtrl
	# If using Fuzzy delete this row:
	print("No Fuzzy Controller!")

def configNN(self,pars):
	# ------ NN controller --
	self.loaded_model=keras.models.load_model("YZ2ZBA.hdf5")
	for i in range(len(self.loaded_model.layers)):
		self.neurons += self.loaded_model.get_layer(index=i).units

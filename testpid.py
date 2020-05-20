import numpy as np
import matplotlib.pyplot as plt
from pendlib import pend
import gym
import os

#Test call from windows console:
#python -c "import testpid; testpid.testpid([-0.32711335, 0.01494436, -0.83031959, -0.00398567, 0.01237051, -0.28880158])"
def testpid(pars):
	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
	# pend(pars,simulation_time,save)
	pend(pars,250,1)


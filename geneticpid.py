import numpy as np
#import pandas as pd
from pendlib import pend

def geneticpid(pars,gen):
	ret=0
	#data = genfromtxt("values.csv", delimiter=',')

	#ret = pend(pars,50+(gen-1)*10,0)
	ret = pend(pars,200,0)

	return ret

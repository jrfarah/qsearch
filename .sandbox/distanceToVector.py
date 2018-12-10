import numpy as np
import scipy.optimize
import random

## input ##
# elementArray = []

def objectiveFunction(elementArray):
	onevec = np.array([1 for x in range(len(elementArray)/2)])
	return np.linalg.norm(onevec - np.array(elementArray))


minimizedVector = scipy.optimize.minimize(objectiveFunction, [random.random() for x in range(3)], options={'disp':True, })

print minimizedVector.x

## output ##
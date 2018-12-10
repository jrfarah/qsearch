import numpy
import mathBackBone
from decimal import *
import scipy.optimize
import FramePotential

def findFiducial(d=3, framepotential=FramePotential.framePotentialReal, return_info=False):
    startingVector  = mathBackBone.generateSeparatedRandomVector(d).elements
    minimizedVector = scipy.optimize.minimize(framepotential, startingVector, method='SLSQP', options={'maxiter':1000, 'ftol':Decimal(10**(-50))})
    if return_info == True: return minimizedVector
    return minimizedVector.x

   
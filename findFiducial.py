import numpy
import mathBackBone
import scipy.optimize
import FramePotential

def findFiducial(d=3, framepotential=FramePotential.framePotentialReal, return_info=False):
    startingVector  = mathBackBone.generateSeparatedRandomVector(d).elements
    minimizedVector = scipy.optimize.minimize(FramePotential.framePotentialReal, startingVector, options={'maxiter':1000})
    if return_info == True: return minimizedVector
    return minimizedVector.x
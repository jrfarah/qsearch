import numpy
import mathBackBone
import scipy.optimize
import FramePotential

def findFiducial(d=3):
    startingVector  = mathBackBone.generateSeparatedRandomVector(d).elements
    minimizedVector = scipy.optimize.minimize(FramePotential.framePotentialReal, startingVector, options={'maxiter':1000})
    return minimizedVector.x
import time
import numpy
import random
import findFiducial
import mathBackBone
import FramePotential

## TODO
# phase freedom of first element is removed 
# restructure frame potentials to be less moronic

def gTest():
    for i in range(4):
        for k in range(4):
            print mathBackBone.gMatrixElement((1./2)*numpy.array([1, 0, 0, 1, 1/numpy.sqrt(2), (-1/numpy.sqrt(2))*1, 0, -1]), i, k),
        print '\n'

def generateRandomVector(d):
    elems = [complex(random.random(), random.random()) for i in range(d)]
    vec = mathBackBone.vector(elems)
    print list(vec.elements)
    return vec

def standardMatrixTest():
    print mathBackBone.w()
    print mathBackBone.I(d=3).matrix
    print mathBackBone.X(d=3).matrix
    print mathBackBone.Z(d=3).matrix
    print mathBackBone.X(d=3).dot(mathBackBone.Z(d=3))

def framePotentialTest():
    return FramePotential.framePotential(generateRandomVector(3))

def framePotentialTest2():
    testVec = mathBackBone.vector([0.0723391 - 0.19082j, 0.0792411 + 0.2153j, 0.536444 + 0.199117j, 0.137276 + 0.0599187j, -0.312771 - 0.439084j, 0.447471 + 0.254983j]) ## frame potential should be 2.27671
    return FramePotential.framePotential(testVec)

def minimizationTest():
    return findFiducial.findFiducial(d=2, framepotential=FramePotential.framePotential3d2Separated, return_info=True)

def sicTest():
    sic = (1./numpy.sqrt(2.))*numpy.array([1, 0, -1, 0, 0, 0])
    print mathBackBone.vector(sic).elements
    print FramePotential.framePotentialReal(sic)

def main():
    '''tests to run'''
    t0 = time.time()
    vec = minimizationTest()
    print "VECTOR RESULT", vec.x
    print "Analysis of minimization: ", vec
    print "Frame potential of minimized vector", FramePotential.framePotentialSeparated(vec.x)
    print "NORM", numpy.linalg.norm(vec.x)
    # print "HI", FramePotential.framePotential3d2nonMinimize(vec.x)
    t1 = time.time()
    print "Elapsed time: ", t1-t0
    # print "Frame potential xof random vector: \n", framePotentialTest()
    # gTest()
    # print FramePotential.framePotentialSeparated(minimizationTest())
    # sicTest()
    # standardMatrixTest()

if __name__ == '__main__':
    main()

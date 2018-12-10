import mathBackBone
import numpy 
from decimal import *
import time

def framePotential(vec):
    ## get frame potential from a VECTOR OBJECT ##
    d = vec.length
    framePotentialSum = 0
    for k in range(d):
        for l in range(d):
            # middleOperator = mathBackBone.matrix(mathBackBone.X(d=d, power=k).dot(mathBackBone.Z(d=d, power=l)), size=d)
            # middleOperatorDotVector = mathBackBone.vector(middleOperator.dot(vec))
            # framePotentialSum += numpy.abs(mathBackBone.vector(vec.conjugate).dot(middleOperatorDotVector))**4
            XpowerK = mathBackBone.X(d = d, power = k)
            ZpowerL = mathBackBone.Z(d = d, power = l)
            # print "X", XpowerK.matrix
            # print "Z", ZpowerL.matrix
            conjugateVector = mathBackBone.vector(vec.conjugate)
            lastTwo = mathBackBone.vector(ZpowerL.dot(vec))
            # print "Last two: ", lastTwo.elements
            lastThree = mathBackBone.vector(XpowerK.dot(lastTwo))
            # print "Last three:", lastThree.elements
            # print conjugateVector.dot(lastThree)
            framePotentialSum += abs(conjugateVector.dot(lastThree))**4


    return framePotentialSum

def framePotentialReal(elementArray):
    ## (MINIMIZE) get frame potential from a FLATTENED ELEMENT ARRAY ##
    d = len(elementArray)/2
    vec = elementArray
    elements = []
    for i in range(0, len(elementArray)-1, 2):
        # print "REAL", elementArray[i]
        # print "COMPLEX", elementArray[i+1]
        elements.append(complex(elementArray[i], elementArray[i+1]))

    vec = mathBackBone.vector(elements)
    framePotentialSum = 0
    for k in range(d):
        for l in range(d):
            # middleOperator = mathBackBone.matrix(mathBackBone.X(d=d, power=k).dot(mathBackBone.Z(d=d, power=l)), size=d)
            # middleOperatorDotVector = mathBackBone.vector(middleOperator.dot(vec))
            # framePotentialSum += numpy.abs(mathBackBone.vector(vec.conjugate).dot(middleOperatorDotVector))**4
            XpowerK = mathBackBone.X(d = d, power = k)
            ZpowerL = mathBackBone.Z(d = d, power = l)
            # print "X", XpowerK.matrix
            # print "Z", ZpowerL.matrix
            conjugateVector = mathBackBone.vector(vec.conjugate)
            lastTwo = mathBackBone.vector(ZpowerL.dot(vec))
            # print "Last two: ", lastTwo.elements
            lastThree = mathBackBone.vector(XpowerK.dot(lastTwo))
            # print "Last three:", lastThree.elements
            # print conjugateVector.dot(lastThree)
            framePotentialSum += abs(conjugateVector.dot(lastThree))**4


    return ((framePotentialSum) - (2.*d/(d+1.)))**2. + (1.-numpy.linalg.norm(vec.elements))**2

def framePotentialSeparated(elementArray):
    ##  get frame potential from a FLATTENED ELEMENT ARRAY ##
    d = len(elementArray)/2
    elements = []
    for i in range(0, len(elementArray)-1, 2):
        elements.append(elementArray[i] + elementArray[i+1]*1j)
    vec = mathBackBone.vector(elements)
    framePotentialSum = 0
    for k in range(d):
        for l in range(d):
            # middleOperator = mathBackBone.matrix(mathBackBone.X(d=d, power=k).dot(mathBackBone.Z(d=d, power=l)), size=d)
            # middleOperatorDotVector = mathBackBone.vector(middleOperator.dot(vec))
            # framePotentialSum += numpy.abs(mathBackBone.vector(vec.conjugate).dot(middleOperatorDotVector))**4
            XpowerK = mathBackBone.X(d = d, power = k)
            ZpowerL = mathBackBone.Z(d = d, power = l)
            # print "X", XpowerK.matrix
            # print "Z", ZpowerL.matrix
            conjugateVector = mathBackBone.vector(vec.conjugate)
            lastTwo = mathBackBone.vector(ZpowerL.dot(vec))
            # print "Last two: ", lastTwo.elements
            lastThree = mathBackBone.vector(XpowerK.dot(lastTwo))
            # print "Last three:", lastThree.elements
            # print conjugateVector.dot(lastThree)
            framePotentialSum += abs(conjugateVector.dot(lastThree))**4

    return framePotentialSum

def framePotential3d2(elementArray):
    ## (MINIMIZE) get frame potential via 2d/d+1 from REAL vector ##
    framePotentialSum = 0
    for j in range(len(elementArray)):
        for k in range(3):
            framePotentialSum += abs((((mathBackBone.kDelta(j, 0) + mathBackBone.kDelta(k, 0))/(len(elementArray) + 1)) - mathBackBone.gMatrixElement(elementArray, j, k)**2)) 
    return framePotential3d2

def framePotential3d2Separated(elementArray):
    ## (MINIMIZE) get frame potential via 2d/d+1 from a FLATTENED ELEMENT ARRAY ##
    d = len(elementArray)/2
    vec = elementArray
    elements = []
    for i in range(0, len(elementArray)-1, 2):
        # print "REAL", elementArray[i]
        # print "COMPLEX", elementArray[i+1]
        elements.append(complex(elementArray[i], elementArray[i+1]))

    # print ((mathBackBone.kDelta(0, 0) + mathBackBone.kDelta(0, 0))/(d + 1)) 
    framePotentialSum = 0
    for l in range(len(elements)):
        for k in range(3):
            framePotentialSum += abs((((mathBackBone.kDelta(l, 0) + mathBackBone.kDelta(k, 0))/(d + 1)) - mathBackBone.gMatrixElement(elementArray, l, k))**2) 

    return framePotentialSum + (1-numpy.linalg.norm(elements))**2

def framePotential3d2nonMinimize(elementArray):
    ## (MINIMIZE) get frame potential via 2d/d+1 from REAL vector ##
    d = len(elementArray)/2
    elements = []
    for i in range(0, len(elementArray)-1, 2):
        # print "REAL", elementArray[i]
        # print "COMPLEX", elementArray[i+1]
        elements.append(complex(elementArray[i], elementArray[i+1]))

    framePotentialSum = 0
    for j in range(len(elements)):
        for k in range(3):
            framePotentialSum += abs(mathBackBone.gMatrixElement(elementArray, j, k))

    return framePotentialSum

# def framePotential3d2SeparatedNonMinimize(elementArray):


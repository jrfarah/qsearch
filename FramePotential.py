import mathBackBone
import numpy 

def framePotential(vec):
    # vec.normalize()
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
    # vec.normalize()
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


    return (framePotentialSum - (2.*d/(d+1.)))**2. + (1.-numpy.linalg.norm(vec.elements))**2

def framePotentialSeparated(elementArray):
    # vec.normalize()
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
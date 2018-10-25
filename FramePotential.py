import mathBackBone
import numpy 

def framePotential(vec):
	d = vec.length
	framePotentialSum = 0
	for k in range(d):
		for l in range(d):
			middleOperator = mathBackBone.matrix(mathBackBone.X(d=d, power=k).dot(mathBackBone.Z(d=d, power=l)), size=d)
			middleOperatorDotVector = mathBackBone.vector(middleOperator.dot(vec))
			framePotentialSum += numpy.abs(mathBackBone.vector(vec.conjugate).dot(middleOperatorDotVector))**4

	return framePotentialSum
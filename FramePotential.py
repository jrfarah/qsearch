import mathBackBone

def framePotential(vec):
	d = vec.length
	print d
	framePotentialSum = 0
	for k in range(0, d):
		for l in range(0, d):
			# framePotentialSum += vec.conjugate.dot(mathBackBone.X(d=d, power=k).dot(mathBackBone.Z(d=d, power=l).dot(vec)))
			middleOperator = mathBackBone.matrix(mathBackBone.X(d=d, power=k).dot(mathBackBone.Z(d=d, power=l)))
			print middleOperator.matrix
			middleOperatorDotVector = middleOperator.vector(middleOperator.dot(vec))
			framePotentialSum += vector(vec.conjugate).dot(middleOperatorDotVector)

	return framePotentialSum
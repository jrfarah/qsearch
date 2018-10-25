import random
import numpy
import mathBackBone
import FramePotential

## TODO
# enforce that the magnitude will always be normalized, phase freedom of first element is removed 

def generateRandomVector(d):
	elems = [complex(random.random() + random.random()*1j) for i in range(d)]
	vec = mathBackBone.vector(elems).normalize()
	print list(vec.elements)
	return vec

def standardMatrixTest():
	print mathBackBone.w()
	print mathBackBone.I().matrix
	print mathBackBone.X(d=3).matrix
	print mathBackBone.Z(d=3).matrix
	print mathBackBone.X(d=3).dot(mathBackBone.Z(d=3))

def framePotentialTest():
	return FramePotential.framePotential(generateRandomVector(5))

def framePotentialTest2():
	testVec = mathBackBone.vector([0.0723391 - 0.19082j, 0.0792411 + 0.2153j, 0.536444 + 0.199117j, 0.137276 + 0.0599187j, -0.312771 - 0.439084j, 0.447471 + 0.254983j]) ## frame potential should be 2.27671
	return FramePotential.framePotential(testVec)

def main():
	'''tests to run'''
	print "Frame potential of specific vector: \n", framePotentialTest2()
	# standardMatrixTest()

if __name__ == '__main__':
	main()

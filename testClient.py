import random
import numpy
import mathBackBone
import FramePotential

## TODO
# enforce that the magnitude will always be normalized, phase freedom of first element is removed 

def generateRandomVector(d):
	elems = [complex(random.random() + random.random()*1j) for i in range(d)]
	return mathBackBone.vector(elems)

def standardMatrixTest():
	print mathBackBone.w()
	print mathBackBone.I().matrix
	print mathBackBone.X(d=3).matrix
	print mathBackBone.Z(d=3).matrix
	print mathBackBone.X(d=3).dot(mathBackBone.Z(d=3))

def framePotentialTest():
	print FramePotential.framePotential(generateRandomVector(5))

def main():
	'''tests to run'''
	framePotentialTest()
	# standardMatrixTest()

if __name__ == '__main__':
	main()

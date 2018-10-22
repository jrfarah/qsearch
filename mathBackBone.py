import numpy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class vector(object):

	def __init__(self, elements, length=False):
		self.elements 	= numpy.array(elements)
		self.transpose 	= self.transpose()
		self.conjugate  = self.conjugate()
		self.type 		= 'vector'

		if length is not True:
			self.length = len(self.elements)
		else: 
			self.length = length



	def dot(self, that):
		''' return the dot product of self vector with that vector '''
		if that.length != self.length: 
			print bcolors.WARNING + "[Cannot perform dot product. len(A) =/= len(B).]" + bcolors.ENDC

		if that.type == 'matrix':
			return numpy.dot(self.elements, that.matrix)

		s = 0
		for i, element in enumerate(self.elements):
			s += element * that.elements[i]

		return s

	def transpose(self):
		return numpy.array([[element] for element in self.elements])

	def conjugate(self):
		return numpy.conjugate(self.elements)


class matrix(object):

	def __init__(self, elements, size=False):
		self.elements 	= elements
		print elements
		self.type 		= 'vector'
		if size is not True: 
			self.size 	= (int(size), int(size))
		else:
			self.size 	= ( numpy.sqrt(len(self.elements)), numpy.sqrt(len(self.elements)) )

		self.matrix 	= self.elements.reshape(self.size)
		self.transpose 	= self.transpose()
		self.conjugate  = self.conjugate()


	def dot(self, that):
		''' matrix multiply two matrices'''
		return numpy.dot(self.matrix, that.matrix)


	def transpose(self):	
		return numpy.transpose(self.matrix)

	def conjugate(self):
		return numpy.conjugate(self.matrix)

def w(d = 2):
	return numpy.exp(2. * numpy.pi * 1j / d)

def I(d = 2):
	tempI = numpy.identity(d)
	return matrix(tempI.flatten(), size=d)

def X(d = 2, power = 1):
	tempX = numpy.linalg.matrix_power(numpy.roll(I(d).matrix, -1), power)
	return matrix(tempX.flatten(), size=d)

def Z(d = 2, power = 1):
	mulitiplicativeVector = vector([numpy.power(w(d), k) for k in range(0, d)])
	identity = I(d)
	tempZ = numpy.linalg.matrix_power((identity.transpose * mulitiplicativeVector.elements).T, power)
	return matrix(tempZ.flatten(), size=d)



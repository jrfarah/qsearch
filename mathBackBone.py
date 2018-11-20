import numpy
import random
from decimal import *

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
        self.elements   = numpy.array(elements)
        self.transpose  = self.transpose()
        self.conjugate  = self.conjugate()
        self.type       = 'vector'

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

    def normalize(self):
        magnitude = numpy.sum(self.elements**2)**0.5
        self.elements = self.elements/magnitude
        print bcolors.OKGREEN + "Normalized vector!" + bcolors.ENDC
        return self


class matrix(object):

    def __init__(self, elements, size=False):
        self.elements   = elements
        self.type       = 'vector'
        if size is not False: 
            self.size   = (int(size), int(size))
        else:
            self.size   = ( int(numpy.sqrt(len(self.elements))), int(numpy.sqrt(len(self.elements))) )

        self.matrix     = self.elements.reshape(self.size)
        self.transpose  = self.transpose()
        self.conjugate  = self.conjugate()


    def dot(self, that):
        ''' matrix multiply two matrices'''
        try: 
            return numpy.dot(self.matrix, that.matrix)
        except AttributeError:
            return numpy.dot(self.matrix, that.elements)


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
    tempX = numpy.zeros((d, d))
    for i in range(d):
        for j in range(d):
            if (i - j + 1) % d == 0:
                tempX[i][j] = 1
    tempX = numpy.linalg.matrix_power(tempX, power)
    return matrix(tempX.flatten(), size=d)

def Z(d = 2, power = 1):
    mulitiplicativeVector = vector([numpy.power(w(d), k) for k in range(0, d)])
    identity = I(d)
    tempZ = numpy.linalg.matrix_power((identity.transpose * mulitiplicativeVector.elements).T, power)
    return matrix(tempZ.flatten(), size=d)

def generateRandomVector(d):
    elems = numpy.array([complex(random.random(), random.random()) for i in range(d)])
    elems = elems/numpy.sum(elems**2)**0.5
    vec = vector(elems)
    # print list(vec.elements)
    return vec

def generateSeparatedRandomVector(d):
    elems = []
    for i in range(d*2):
        elems.append(Decimal(random.random()))
    return vector(elems)

def generatedInflatedVector(elementArray):
    elems = []
    for i in range(len(elementArray) - 1):
        elems.append(elementArray[i] + elementArray[i+1]*1j)
        i += 1
    return elems

def gMatrixElement(elementArray, j, k):
    vec = elementArray
    elements = []
    for i in range(0, len(elementArray)-1, 2):
        elements.append(elementArray[i] + elementArray[i+1]*1j)

    val = 0
    for s in range(len(elements)):
        # val += 
        val += numpy.conjugate(elements[s % len(elements)]) * elements[(s + j) % len(elements)] * elements[(s + k) % len(elements)] * numpy.conjugate(elements[(s + j + k) % len(elements)])

    return val

def kDelta(i, j):
    if i == j:  return 1
    else:       return 0 
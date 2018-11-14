import matplotlib.pyplot as plt 
import seaborn as sns
import itertools
import glob
import time
import sys

import time
import numpy
import random
import findFiducial
import mathBackBone
import FramePotential


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rcParams.update({'font.size': 16})
plt.rcParams['axes.linewidth'] = 2 #set the value globally
plt.rcParams["font.weight"] = "bold"
plt.rcParams['text.latex.preamble'] = [r'\usepackage{sfmath} \boldmath']
cycol = itertools.cycle(sns.color_palette())

def minimizationTest(d):
    return findFiducial.findFiducial(d=d, framepotential=FramePotential.framePotential3d2Separated)

def main(maxd):
    times = []
    for d in range(1, maxd):
        print "Dimension: ", d
        t0 = time.time()
        print FramePotential.framePotentialSeparated(minimizationTest(d))
        t1 = time.time()
        print "Elapsed time (sec): ", t1-t0
        times.append(t1-t0)

    plt.plot(range(1, maxd), times)
    plt.show()


if __name__ == '__main__':
    main(int(sys.argv[1]))
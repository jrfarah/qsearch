import os
import sys
import numpy as np

def generate_new_table(d):
    with open("dim.dim", "w") as dim:
        dim.write(str(d)+"\n")
    os.system("rm -f table2.csv")
    command = './minimal_3d2.wls'
    os.system(command)

    with open("table2.csv", 'r') as f:
      lines = f.readlines()

    lines = [i.replace('\t', ', ').replace('^', 'e').replace('I','j').replace('*', '').replace("0.j", "0.0j").split(',') for i in lines][0]

    dim = int(len(lines)**0.5)
    print dim

    table = lines
    # table = np.reshape(lines, (dim, dim))

    return table

for i in range(100):
    generate_new_table(sys.argv[1])
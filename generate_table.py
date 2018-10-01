import os
import sys

def generate_new_table(d):
    global global_table
    with open("dim.dim", "w") as dim:
        dim.write(str(d)+"\n")
    os.system("rm -f table2.csv")
    command = './minimal_3d2.wls'
    print command
    os.system(command)

    with open("table2.csv", 'r') as f:
      lines = f.readlines()

    lines = [i.replace('\t', ', ').replace('^', 'e').replace('I','j').replace('*', '').replace("0.j", "0.0j").split(',') for i in lines][0]

    print lines

for i in range(100):
    generate_new_table(sys.argv[1])
import os
import csv


def evaluate(var, dir="./"):
    # set value
    with open("{}/MOP/pop_vars_eval.txt".format(dir), "w") as f:
        for x in var:
            f.write("{}\t".format(x))

    # calc
    os.system(
        "/home/nakata/compe2019/compe2019/bin/python ./windturbine_MOP.py ./MOP/")

    # get value
    eVal = []
    with open("{}/MOP/pop_objs_eval.txt".format(dir), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for t in row[0].split("\t"):
                eVal.append(float(t))
            break

    # get value
    cs = []
    with open("{}/MOP/pop_cons_eval.txt".format(dir), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for t in row[0].split("\t"):
                cs.append(float(t))
            break

    return eVal,cs


if __name__ == "__main__":
    var = [0.5 for _ in range(32)]
    e = evaluate(var, dir="./")
    print(e)

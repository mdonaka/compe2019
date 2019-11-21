import os
import csv


class compe2019:

    def __init__(self, dir="./"):
        self.__dir = dir
        self.__count = 0

    def __getLineFromFile(self, fileName):
        vals = []
        with open("{}/MOP/{}.txt".format(self.__dir, fileName), "r") as f:
            reader = csv.reader(f)
            for row in reader:
                for t in row[0].split("\t"):
                    vals.append(float(t))
                break
        return vals

    def f(self, var):

        # evaluation count increment
        self.__count += 1

        # set value
        with open("{}/MOP/pop_vars_eval.txt".format(self.__dir), "w") as f:
            for x in var:
                f.write("{}\t".format(x))

        # calc
        os.system(
            "/home/nakata/compe2019/compe2019/bin/python {0}/MOP/windturbine_MOP.py {0}/MOP/".format(self.__dir))

        # get values
        objs = self.__getLineFromFile("pop_objs_eval")
        cons = self.__getLineFromFile("pop_cons_eval")

        return objs, cons


if __name__ == "__main__":
    compe = compe2019()
    var = [0.5 for _ in range(32)]
    o, c = compe.f(var)
    print(o, c)

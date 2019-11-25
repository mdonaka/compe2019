import os
import csv
from logging import getLogger
logger = getLogger(__name__)

__author__ = "R.Nakata"
__date__ = "2019/11/21"


class compe2019:
    """
    EC symposium 2019 competition Benchmark Function

    attributes
    ----------
    dir : str
        competiion data directory
    count : int
        evaluation count
    problem : str
        target problem is MOP or SOP
    """

    def __init__(self, dir="./", isMOP=True):
        """
        Parameters
        ---------
        dir : str
            competiion data directory
        isMOP : Boolean
            True: MOP, False: SOP
        """
        self.__dir = dir
        self.__count = 0
        self.__problem = "MOP" if isMOP else "SOP"

    def __getLineFromFile(self, fileName):
        """
        get result of evaluation

        Parameters
        ---------
        fileName : str
            file name of values
        """
        vals = []
        with open("{}/{}/{}.txt".format(self.__dir, self.__problem, fileName), "r") as f:
            reader = csv.reader(f)
            for row in reader:
                for t in row[0].split("\t"):
                    vals.append(float(t))
                break
        return vals

    def f(self, var):
        """
        evaluate Benchmark function

        Parameters
        ---------
        var : list<float>
            design variables
        """

        # evaluation count increment
        self.__count += 1

        # set value
        with open("{}/{}/pop_vars_eval.txt".format(self.__dir, self.__problem), "w") as f:
            for x in var:
                f.write("{}\t".format(x))

        # calc
        os.system(
            "/home/nakata/compe2019/compe2019/bin/python {0}/{1}/windturbine_{1}.py {0}/{1}/".format(self.__dir, self.__problem))

        # get values
        objs = self.__getLineFromFile("pop_objs_eval")
        cons = self.__getLineFromFile("pop_cons_eval")

        print(",".join(map(str, objs)))
        print(",".join(map(str, cons)))

        return objs


if __name__ == "__main__":
    compe = compe2019()
    var = [0.5 for _ in range(32)]
    o, c = compe.f(var)
    print(o, c)

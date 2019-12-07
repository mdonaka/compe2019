from pyDOE import lhs
from logging import getLogger, basicConfig, DEBUG
from platypus import Problem, Real, MOEAD
import numpy as np
logger = getLogger(__name__)


class RandomSearch:
    def __init__(self, dim, obj, f):
        self.dim = dim
        self.obj = obj
        self.f = f
        self.ran = [[0.0, 1.0] for _ in range(dim)]
        pass

    def run(self, n=10000):
        comp = [1000, 1000, 1000, 500, 500]
        comp = [10, 10, 10, 50, 50]
        for c in comp:
            x,y = self.generateLHS(c)
            self.ranComp(x,y)
            logger.debug(self.ran)

    def generateLHS(self, size=1000):
        x = [[s[i] for i in range(self.dim)] for s in lhs(self.dim, size, "c")]
        for t in x:
            for i, r in enumerate(self.ran):
                t[i] *= (r[1]-r[0])
                t[i] += r[0]
        y = [self.f(t) for t in x]
        return x, y

    def ranComp(self, x, y):
        z = [[a, b] for a, b in zip(x, y)]
        xlst = []
        for i in range(self.obj):
            f = sorted(z, key=lambda t: t[1][i])
            for j in range(len(f)):
                flg = True
                for val in xlst:
                    if val == f[j][0]:
                        flg = False
                if flg:
                    xlst.append(f[j][0])
                    break
        for i in range(self.obj):
            l = [t[i] for t in xlst]
            l = sorted(l)
            it = 0
            dif = l[2]-l[0]
            for j in range(1, self.obj-2):
                d = l[j+2]-l[j]
                if d < dif:
                    it = j
                    dif = d
            self.ran[i] = [l[it], l[it+2]]


    def show(self):
        for sol in self.algorithm.result:
            logger.debug(sol.objectives)


if __name__ == "__main__":
    basicConfig(level=DEBUG)

    def f(x):
        val = [np.sum(x), 30-np.sum(x), np.sum(x), np.sum(x)]
        print(val)
        return val

    # rs = RandomSearch(32, 5, f)
    rs = RandomSearch(4, 4, f)
    rs.run()

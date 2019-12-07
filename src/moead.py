from logging import getLogger, basicConfig, DEBUG
from platypus import Problem, Real, MOEAD
logger = getLogger(__name__)

class MOEA_D:
    def __init__(self, des, obj, f, r):
        self.problem = Problem(des,obj)
        self.problem.types[:] = r#Real(0.0,1.0)
        self.problem.function = f
        self.algorithm = MOEAD(self.problem)

    def run(self, n=10000):
        self.algorithm.run(n)

    def show(self):
        for sol in self.algorithm.result:
            logger.debug(sol.objectives)




if __name__ == "__main__":
    basicConfig(level=DEBUG)




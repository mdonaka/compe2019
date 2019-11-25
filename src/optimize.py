from logging import getLogger, basicConfig, DEBUG
from platypus import Problem, Real, MOEAD
logger = getLogger(__name__)

class algorithm:
    def __init__(self, des, obj, f):
        self.problem = Problem(1,2)
        self.problem.types[:] = Real(-1.0,1.0)
        self.problem.function = f
        self.algorithm = MOEAD(self.problem)

    def run(self):
        algorithm.run(200)

    def show(self):
        for sol in algorithm.result:
            logger.debug(sol.objectives)




if __name__ == "__main__":
    basicConfig(level=DEBUG)




from logging import getLogger, basicConfig, DEBUG
from platypus import Problem, Real, MOEAD
logger = getLogger(__name__)


class RandomSearch:
    def __init__(self, des, obj, f):
        pass

    def run(self, n=10000):
        pass

    def show(self):
        for sol in self.algorithm.result:
            logger.debug(sol.objectives)


if __name__ == "__main__":
    basicConfig(level=DEBUG)

    def f(x):
        return 1

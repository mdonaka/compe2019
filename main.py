from logging import getLogger, basicConfig, DEBUG
from src.iniitalze import generate
from src.function import compe2019
from src.optimize import algorithm
logger = getLogger(__name__)


if __name__ == '__main__':
    basicConfig(level=DEBUG)
    logger.debug("-- start --")

    compe = compe2019()
    f = compe.f

    alg = algorithm(32,5,f)
    alg.run(30)

    alg.show()

from logging import getLogger, basicConfig, DEBUG
from src.iniitalze import generate
from src.function import compe2019
from src.moead import MOEA_D
from src.randomSearch import RandomSearch
logger = getLogger(__name__)


if __name__ == '__main__':
    basicConfig(level=DEBUG)
    logger.debug("-- start --")

    th = input()
    compe = compe2019(thread=th)
    f = compe.f

    #alg = MOEA_D(32,5,f)
    alg = RandomSearch(32,5,f)
    alg.run(10000)

    alg.show()

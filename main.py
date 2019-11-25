from logging import getLogger, basicConfig, DEBUG
from src.iniitalze import generate
from src.function import compe2019
logger = getLogger(__name__)


if __name__ == '__main__':
    basicConfig(level=DEBUG)
    logger.debug("-- start --")

    vars = generate(3)

    f = compe2019().f
    for var in vars:
        e, c = f(var)

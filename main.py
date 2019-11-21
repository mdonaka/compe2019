from iniitalze import generate
from function import compe2019


def addC(c):
    with open("./test/con.csv", "a") as f:
        for p in c:
            f.write("{}\t".format(p))
        f.write("\n")


def addE(e):
    with open("./test/eva.csv", "a") as f:
        for p in e:
            f.write("{}\t".format(p))
        f.write("\n")


if __name__ == '__main__':
    vars = generate(1)
    f = compe2019().f

    for var in vars:
        e, c = f(var)
        addC(c)
        addE(e)
        print(e)

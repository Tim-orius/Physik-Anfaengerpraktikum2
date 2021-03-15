"""Small program for calculations with capacitys of condensators"""

class Cond():
    """Class for Condensators"""

    def __init__(self, c):
        """Constructor"""
        self.c =  c

    def reihe(self, caps: list):
        """Reiehnschaltung"""

        values = [1 / caps[i].c for i in range(len(caps))]
        values.append(1 / self.c)
        return 1 / sum(values)

    def para(self, caps: list):
        """Parallelschaltung"""

        values = [caps[i].c for i in range(len(caps))]
        values.append(self.c)
        return sum(values)


def main():
    """Initialise some capacitys"""

    global c1, c2, cpa, creih, cl, cr_p, cr, cges

    c1 = Cond(102.395*10**(-6))
    c2 = Cond(15.284*10**(-6))
    cpa = Cond(c1.para([c2]))
    creih = Cond(c1.reihe([c2]))

    cl = Cond(c2.reihe([c1, c2]))
    cr_p = Cond(c1.para([c2]))
    cr = Cond(c1.reihe([cr_p, c1, c2]))
    cges = Cond(cl.para([cr]))


if __name__ == "__main__":
    main()

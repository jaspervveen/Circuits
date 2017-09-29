

class BuildCircuit:

    def __init__(self):
        pass

    def zr(self, r):
        return r

    def zc(self, w, c):
        return 1/(1j*w*c)

    def zl(self, w, l):
        return 1j*w*l

    def add_parallel(self, z1, z2):
        return 1/(1/z1+1/z2)

    def add_series(self, z1, z2):
        return z1 + z2

    def calc_gamma(self, zt, zl):
        return (zl-zt)/(zl+zt)
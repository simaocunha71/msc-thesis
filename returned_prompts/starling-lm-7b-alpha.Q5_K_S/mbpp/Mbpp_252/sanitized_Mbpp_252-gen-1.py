import math
def convert(n):
    r = math.sqrt(n.real ** 2 + n.imag ** 2)
    theta = math.atan2(n.imag, n.real)
    return r, theta
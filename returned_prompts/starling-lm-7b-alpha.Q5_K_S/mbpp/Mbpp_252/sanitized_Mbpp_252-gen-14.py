import cmath
def convert(c):
    r = abs(c)
    theta = cmath.phase(c)
    return (r, theta)
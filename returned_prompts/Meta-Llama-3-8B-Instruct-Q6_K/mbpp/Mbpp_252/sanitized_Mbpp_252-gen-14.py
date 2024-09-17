import cmath
def convert(z):
    r = abs(z)
    theta = cmath.phase(z)
    return (r, theta)
import cmath
def convert(n):
    r, theta = cmath.polar(n)
    return (r, theta)
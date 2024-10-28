import cmath
def convert(x):
    r = cmath.polar(x)[0]
    theta = cmath.polar(x)[1]
    return (r, theta)
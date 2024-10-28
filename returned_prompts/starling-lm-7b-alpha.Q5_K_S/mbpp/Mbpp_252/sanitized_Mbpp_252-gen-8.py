import cmath
def convert(x):
    mag = cmath.polar(x)[0]
    angle = cmath.polar(x)[1]
    return (mag, angle)
import cmath
def convert(complex_number):
    magnitude, angle = cmath.polar(complex_number)
    return (magnitude, angle)
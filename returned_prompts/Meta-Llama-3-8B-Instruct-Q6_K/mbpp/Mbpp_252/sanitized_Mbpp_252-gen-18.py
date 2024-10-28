import cmath
import math
def convert(z):
    r = abs(z)
    theta = cmath.phase(z)
    return (r, math.degrees(theta))
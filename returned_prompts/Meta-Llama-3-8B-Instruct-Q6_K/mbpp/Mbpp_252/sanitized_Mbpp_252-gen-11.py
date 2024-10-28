import cmath
import math
def convert(z):
    r = abs(z)
    theta = math.atan2(z.imag, z.real)
    return (r, theta)
import math
def convert(z):
    if isinstance(z, complex):
        r = abs(z)
        theta = math.atan2(z.imag, z.real)
        return (r, math.degrees(theta))
    else:
        return (1.0, 0.0)
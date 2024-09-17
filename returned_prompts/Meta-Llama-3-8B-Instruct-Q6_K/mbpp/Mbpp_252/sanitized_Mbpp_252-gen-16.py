import math
def convert(c):
    if c.real == 0:
        return (0, 0)
    else:
        magnitude = math.sqrt(c.real**2 + c.imag**2)
        angle = math.atan2(c.imag, c.real)
        return (magnitude, math.degrees(angle))
import math
def convert(num):
    magnitude = abs(num)
    angle = math.atan(num.imag / num.real)
    return (magnitude, angle)
import math
def convert(complex_number):
    real_part = complex_number.real
    imaginary_part = complex_number.imag
    radius = math.sqrt(real_part ** 2 + imaginary_part ** 2)
    angle = math.atan(imaginary_part / real_part)
    if angle < 0:
        angle += math.pi
    return (radius, angle)
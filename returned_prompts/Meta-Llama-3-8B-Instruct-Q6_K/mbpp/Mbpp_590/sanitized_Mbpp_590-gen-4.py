import cmath
def polar_rect(mag, angle):
    angle = cmath.pi / 180 * angle
    x = mag * cmath.cos(angle)
    y = mag * cmath.sin(angle)
    return (x.real, x.imag), (y.real, y.imag) # return both real and imaginary part as tuple
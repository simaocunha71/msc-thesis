import cmath
def polar_rect(r, theta):
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return ((x.real, x.imag), (y.real, y.imag))  # returns both x and y as tuples
import cmath
def polar_rect(r, theta):
    x = r * cmath.cos(cmath.radians(theta))
    y = r * cmath.sin(cmath.radians(theta))
    return (x, y)
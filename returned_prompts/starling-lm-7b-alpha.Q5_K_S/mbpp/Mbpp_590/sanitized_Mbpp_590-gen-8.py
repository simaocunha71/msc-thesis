from math import pi, cos, sin
def polar_rect(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return (x + y * 1j, x - y * 1j)
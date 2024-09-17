def triangle_area(radius):
    if radius < 0:
        return None
    from math import sqrt, pi
    return 0.5 * radius**2 * sqrt(1 - 4/(pi*radius)**2)
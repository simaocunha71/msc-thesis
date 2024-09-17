def triangle_area(radius):
    # The formula to calculate the area of the largest triangle inscribed in a semicircle is given by
    # A = pi * r^2 / (2 * sqrt(2r^2 - r^2))
    # r is the radius of the semicircle
    if radius < 0:
        return None
    else:
        return (2**0.5 * 3.14159265359 * radius**2) / 4
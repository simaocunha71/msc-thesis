def triangle_area(radius):
    if radius < 0:
        return None
    s = radius
    h = (2**0.5) * radius
    area = 0.5 * s * h
    return area
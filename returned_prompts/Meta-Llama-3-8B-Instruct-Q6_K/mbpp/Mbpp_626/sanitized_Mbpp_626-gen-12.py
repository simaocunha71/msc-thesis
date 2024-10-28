def triangle_area(radius):
    if radius < 0:
        return None
    r = radius
    h = (2 * r ** 2) ** 0.5
    a = (h * r) / 2
    return a
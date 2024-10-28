def triangle_area(radius):
    if radius < 0:
        return None
    side = 2 * radius
    s = (side + side + side) / 2
    area = (s * (s - side) * (s - side) / (2 * 3)) ** 0.5
    return area
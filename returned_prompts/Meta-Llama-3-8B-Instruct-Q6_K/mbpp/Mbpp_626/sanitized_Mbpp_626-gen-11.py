def triangle_area(radius):
    if radius < 0:
        return None
    if radius == 0:
        return 0
    side = radius * 2 ** 0.5 / 2
    semiperimeter = side * 2
    s = (2 * side + semiperimeter) / 2
    h = (2 * side * semiperimeter) / (4 * s - side * 2)
    area = (s * (s - side) * (s - semiperimeter)) ** 0.5
    return area
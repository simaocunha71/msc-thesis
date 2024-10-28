def triangle_area(r):
    if r < 0:
        return None
    radius = r
    side = 2 * radius
    area = (1/2) * side * radius
    return area
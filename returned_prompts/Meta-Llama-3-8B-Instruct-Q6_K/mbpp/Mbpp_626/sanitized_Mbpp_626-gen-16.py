def triangle_area(radius):
    if radius < 0:
        return None
    semi_circumference = 2 * radius
    side_length = semi_circumference / 2
    area = (1/2) * side_length * radius
    return area
def triangle_area(radius):
    if radius <= 0:
        return None
    half_radius = radius / 2
    side_length = (2 ** 0.5 - 1) * half_radius
    height = half_radius * (2 ** 0.5)
    area = 0.5 * side_length * height
    return area
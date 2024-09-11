def triangle_area(radius):
    if radius < 0:
        return None
    if radius == 0:
        return 0
    return (1/2) * radius**2
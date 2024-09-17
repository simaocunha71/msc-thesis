def triangle_area(radius):
    if radius < 0:
        return None
    s = radius * 2
    a = (s * (s - radius)) / 2
    return a
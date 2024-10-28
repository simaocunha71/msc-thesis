def triangle_area(radius):
    if radius <= 0:
        return None
    r = radius
    h = math.sqrt(r**2 - (r/2)**2)
    area = (r*h)/2
    return area
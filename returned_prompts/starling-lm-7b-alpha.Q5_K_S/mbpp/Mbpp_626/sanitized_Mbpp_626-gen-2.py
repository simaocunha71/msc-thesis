import math
def triangle_area(radius):
    # Check if the radius is valid
    if radius <= 0:
        return None
    # Calculate the area of the semicircle
    area_semicircle = math.pi * radius ** 2 / 2
    # Calculate the area of the triangle by subtracting the area of the semicircle from the area of the circle
    area_triangle = area_semicircle * 2 / math.pi
    return area_triangle
import math
def triangle_area(r):
    # Calculate the area of the semicircle
    semicircle_area = (1/2) * math.pi * r**2
    # Calculate the area of the largest triangle that can be inscribed in the semicircle
    triangle_area = (1/2) * r * r * math.sqrt(3)
    return triangle_area
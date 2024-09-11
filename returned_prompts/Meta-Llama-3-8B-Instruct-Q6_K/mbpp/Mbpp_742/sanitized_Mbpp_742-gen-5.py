import math
def area_tetrahedron(a):
    area = (1/3) * math.sqrt((a**2)*(a**2+3*a**2))
    return area
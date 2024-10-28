import math
def area_tetrahedron(a):
    s = a / 3
    area = math.sqrt(s * (s - a) * (s - a) * (s - a))
    return area
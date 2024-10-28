import math
def area_tetrahedron(a):
    s = a / 3
    return math.sqrt(3 * math.pow(s, 3)) / math.sqrt(2) * a * a * math.sqrt(3) / 2
import math
def area_tetrahedron(a):
    s = a
    return math.sqrt(3) * s ** 2 / (4 * math.sqrt(s ** 2 + 9))  # a is the length of the edge of the tetrahedron.  # return value is the area of the tetrahedron.
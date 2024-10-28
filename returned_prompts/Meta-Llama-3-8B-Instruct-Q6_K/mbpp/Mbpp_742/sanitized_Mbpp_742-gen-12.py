import math
def area_tetrahedron(p):
    a = 1  # Assuming a, b, c are the lengths of the edges of the tetrahedron
    b = 1
    c = 1
    V = p
    area = math.sqrt(6*V**2*a**2*b**2*c**2)
    return area
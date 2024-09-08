import math
def area_tetrahedron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(4 * s**2 * (s - a)**2 * (s - b)**2 * (s - c)**2) / 4
    return area
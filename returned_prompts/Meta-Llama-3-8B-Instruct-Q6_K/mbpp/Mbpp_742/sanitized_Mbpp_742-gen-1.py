from math import sqrt, pow
def area_tetrahedron(a):
    return sqrt(3)/4 * pow(a,2) * sqrt(1 + 3/sqrt(3))  # a is the edge length of the tetrahedron. The formula is derived from the formula for the area of a triangle: (base * height) / 2. In this case, the base is the length of the edge of the tetrahedron, and the height is the height of the triangle formed by the edge and the center of the tetrahedron. The height is calculated using the Pythagorean theorem, and then the area is calculated using the formula for the area of a triangle. The result is then multiplied by 3 to get the area of the tetrahedron.
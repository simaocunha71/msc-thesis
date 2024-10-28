import math
def area_tetrahedron(a, b, c, d):
    # Calculate the area of the base triangle
    p = (a + b + c) / 2
    base_area = math.sqrt(p*(p-a)*(p-b)*(p-c))

    # Calculate the volume of the tetrahedron
    height = math.sqrt((a-b)**2 + (b-c)**2 + (c-a)**2)
    volume = 1/3 * base_area * height

    # Calculate the area of the tetrahedron
    area = math.sqrt(6 * (base_area**2) / volume)
    return area
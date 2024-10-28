from math import sqrt
def area_tetrahedron(side_length):
    """
    Calculate the area of a tetrahedron given its side length.
    """
    # Calculate the height of the tetrahedron using the Pythagorean theorem
    height = sqrt(3) / 2 * side_length
    
    # Calculate the area of the base triangle
    base_area = sqrt(3) / 4 * side_length ** 2
    
    # Calculate the area of the tetrahedron
    area = base_area + 3 * side_length * height / 2
    
    return area
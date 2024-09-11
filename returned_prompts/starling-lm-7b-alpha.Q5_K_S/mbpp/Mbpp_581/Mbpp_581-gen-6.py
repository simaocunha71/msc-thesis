def surface_Area(a, h):
    return 2*a*h + a*a

# Testing
print(surface_Area(3,4) == 33)







"""
Python program to calculate the surface area of a pyramid
"""

def surface_area(base_edge, height):
    """
    This function is designed to calculate the surface area of a square pyramid
    Parameters:
    base_edge(int): the base edge of the pyramid
    height(int): the height of the pyramid
    Return:
    int: The surface area of the pyramid
    """
    return 2*base_edge*height + base_edge*base_edge

# Testing
print(surface_area(3,4) == 33)




# Using the Pythagorean theorem, it can be shown that the slant height of the pyramid can be calculated by
# h = sqrt(a^2 + h^2)
# The surface area of the pyramid is then
# 2 * base_edge * slant_height + base_edge * base_edge
"""
Python program to calculate the surface area of a pyramid
"""

def surface_area(base_edge, height):
    """
    This function is designed to calculate the surface area of a pyramid
    Parameters:
    base_edge(int): the base edge of the pyramid
    height(int): the height of the pyramid
    Return:
    int: The surface area of the pyramid
    """
    slant_height = height * (base_edge**2 + height**2)**0.5
    return 2*base_edge*slant_height + base_edge*base_edge

# Testing
print(surface_area(3,4) == 33)

"""
Python program to calculate the surface area of a pyramid
"""

def surface_area(base_edge, height):
    """
    This function is designed to calculate the surface area of a pyramid
    Parameters:
    base_edge(int): the base edge of the pyram
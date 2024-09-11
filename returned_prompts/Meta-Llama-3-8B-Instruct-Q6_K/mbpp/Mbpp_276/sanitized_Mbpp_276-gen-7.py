import math
def volume_cylinder(radius, height):
    return math.pi * (radius ** 2) * height
    # The result should be a float value for the volume of the cylinder. The function should be tested with the input (10,5) and the expected output should be a float value close to 1570.7500000000002. The math.isclose function is used for this purpose. The rel_tol parameter is set to 0.001 for the comparison.
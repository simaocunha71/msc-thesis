"""
To find the volume of a cone, use the formula:
V = 1/3 * pi * r^2 * h
where V is the volume, r is the radius of the base, and h is the height of the cone.
"""

import math

def volume_cone(r, h):
    """
    Calculates the volume of a cone given the radius (r) and height (h) of the cone.
    """
    pi = math.pi
    return 1/3 * pi * r**2 * h

# Test the function
assert math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=0.001)

# End of program

"""
In this program, we define a function called volume_cone that takes two parameters: r (the radius of the cone) and h (the height of the cone). Inside the function, we define the value of pi using the math.pi constant from the math module. We then calculate the volume of the cone using the given formula and return the result. The function is tested with the assert statement, which checks if the function returns the expected value for the given radius and height.
"""

"""
To test the function, you can use the assert statement followed by math.isclose(volume_cone(r, h), expected_volume, rel_tol=tolerance) to check if the function returns the expected volume within the specified tolerance. The math.isclose function compares two values and checks if they are approximately equal within the specified tolerance. In this case, we use a relative tolerance of 0.001, which means that the absolute difference between the calculated volume and the expected volume should be less than 0.001 times the expected volume.
"""

"""
By using the math.isclose function, we can ensure that the volume_cone function is accurately calculating the volume of a cone within a specified tolerance. This provides confidence in the correctness and reliability of the function's implementation.
"""

"""
In the end of the program, we simply define the function and test it with the assert statement to verify its correctness. This allows us to ensure that the function is working as expected
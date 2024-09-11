"""
import math

def volume_cone(r, h):
    """
    Calculates the volume of a cone with radius r and height h.
    """
    return (1/3) * math.pi * r**2 * h

# Test
import pytest

@pytest.mark.parametrize("r, h", [(5, 12)])
def test_volume_cone(r, h):
    assert math.isclose(volume_cone(r, h), 314.15926535897927, rel_tol=0.001)
"""

Explanation:
The volume of a cone can be calculated using the formula: 1/3 * pi * r^2 * h
Here we define a function called volume_cone that takes two parameters, r (radius) and h (height). Inside the function, we use the formula to calculate the volume of the cone and return the result.

To test the function, we use the pytest library and the parametrize decorator to provide a set of test cases. In this case, we have only one test case with r = 5 and h = 12. We then use the assert statement to check if the result of calling the volume_cone function with these values is close to the expected result (314.15926535897927) with a relative tolerance of 0.001.

This test ensures that the volume_cone function correctly calculates the volume of a cone with the given radius and height.

"""

def volume_cone(r, h):
    """
    Calculates the volume of a cone with radius r and height h.
    """
    return (1/3) * math.pi * r**2 * h

# Test
import pytest

@pytest.mark.parametrize("r, h", [(5, 12)])
def test_volume_cone(r, h):
    assert math.isclose(volume_cone(r, h), 314.15926535897927, rel_tol=0
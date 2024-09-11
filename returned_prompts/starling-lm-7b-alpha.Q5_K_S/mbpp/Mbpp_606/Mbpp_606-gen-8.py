"""
import math

def radian_degree(degrees):
    return degrees * (math.pi/180)

"""

# This code is incorrect because:
# It doesn't use the math.pi constant which is the exact value of pi (approximately 3.14159)
# It doesn't use a docstring to explain what the function does.
# It doesn't use a unit test to verify the result.

# Here's a corrected version of the code:

import math

def radian_degree(degrees):
    """
    Convert degrees to radians.
    """
    return degrees * (math.pi/180)

# Unit test
def test_radian_degree():
    assert radian_degree(90) == 1.5707963267948966
    print("Test Passed")

test_radian_degree()

"""

This corrected version of the code uses the math.pi constant to get the exact value of pi.
It also uses a docstring to explain what the function does.
And, it includes a unit test to verify the result.

"""

def radian_degree(degrees):
    """
    Convert degrees to radians.
    """
    return degrees * (math.pi/180)

# Unit test
def test_radian_degree():
    assert radian_degree(90) == 1.5707963267948966
    print("Test Passed")

test_radian_degree()

"""

This version of the code is correct. It converts degrees to radians using the math.pi constant to get the exact value of pi, and includes a unit test to verify the result.
"""

"""
This version of the code is incorrect because:
It doesn't use the math.pi constant which is the exact value of pi (approximately 3.14159)
It doesn't use a docstring to explain what the function does.
It doesn't use a unit test to verify the result.

Here's a corrected version of the code:

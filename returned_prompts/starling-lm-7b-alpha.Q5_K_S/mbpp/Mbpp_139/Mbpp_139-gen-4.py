"""
The circumference of a circle can be calculated using the formula C = 2πr, where C is the circumference and r is the radius of the circle. The math.isclose function can be used to check if two floating-point numbers are approximately equal within a given tolerance. The assert statement is used to check if the calculated circumference is approximately equal to the expected result.
"""

circle_circumference = lambda r: 2 * 3.141592653589793 * r

def test_circle_circumference():
    assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)

test_circle_circumference()

"""
This code defines a function circle_circumference that takes the radius of a circle as input and calculates the circumference using the formula C = 2πr. The function test_circle_circumference is used to test the circle_circumference function by checking if the calculated circumference is approximately equal to the expected result within a given tolerance using the math.isclose function. The assert statement is used to check if the condition is true.
"""

# Python Program to find the circumference of a circle
import math

def circle_circumference(r):
    # Formula to find the circumference of a circle is C = 2*pi*r
    return 2 * 3.141592653589793 * r

def test_circle_circumference():
    assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)

test_circle_circumference()

"""
This code defines a function circle_circumference that takes the radius of a circle as input and calculates the circumference using the formula C = 2πr. The function test_circle_circumference is used to test the circle_circumference function by checking if the calculated circumference is approximately equal to the expected result within a given tolerance using the math.isclose function.
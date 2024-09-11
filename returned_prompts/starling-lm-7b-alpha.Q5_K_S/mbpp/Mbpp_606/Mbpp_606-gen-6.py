def radian_degree(x):
    return x*(2*3.14159265358979323846/360)

# Testing
from math import pi
from hypothesis import given, settings, assume, reproduce
from hypothesis.strategies import floats

@given(floats(min_value=0, max_value=360))
@settings(max_examples=1000)
def test_radian_degree(x):
    assert radian_degree(x) == x*(2*pi/360)

test_radian_degree(90)

# Alternatively, you could use a different approach to compute radians
def radian_degree_alt(x):
    return x * (2*3.14159265358979323846/360)

# Testing
from hypothesis import given, settings, assume, reproduce
from hypothesis.strategies import floats

@given(floats(min_value=0, max_value=360))
@settings(max_examples=1000)
def test_radian_degree_alt(x):
    assert radian_degree_alt(x) == x*(2*pi/360)

test_radian_degree_alt(90)

"""
In Python, there are several ways to convert degrees to radians, so don't worry if you don't know how to do it.
Here are a few tips to help you get started:

1. Use the math.radians() function from the math module.
2. Use a conversion factor, like 2*pi/360.
3. Use a library like NumPy, which has a convenient function called np.radians().
4. Write a function to convert degrees to radians, like the ones provided in this answer.

It's important to choose the right approach based on the specific requirements of your project and the tools you have available.
"""

# You can use the provided code as a starting point for your implementation.
# Here are some tips to help you get started:

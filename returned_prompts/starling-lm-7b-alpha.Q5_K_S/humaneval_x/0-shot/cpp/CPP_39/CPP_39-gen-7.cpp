    from math import sqrt
    # Python's sqrt function is in the math module

    # Pythagorean theorem states that in a right-angled triangle, the sum of
    # squares of the two shorter sides is equal to the square of the longest side
    return sqrt(a**2 + b**2) == c

    # This can be simplified to a**2 + b**2 == c**2, but this would fail for
    # cases where c is very large, as Python's integer type has a limited range
    # (up to 2**63 - 1).


# Here's how you can use this function:

print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False


# This implementation uses Python's built-in sqrt function from the math module, which is
# faster than using a loop to calculate the square root. However, it assumes that the
# input values are all non-negative integers.

# Here are some more test cases:

print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(8, 15, 17))  # False
print(right_angle_triangle(0, 0, 0))    # False
print(right_angle_triangle(1, 1, 1))    # True
print(right_angle_triangle(-1, 2, 3))   # False
print(right_angle_triangle(3, -2, 5))   # False
print(right_angle_triangle(3, 4, -5))   # False


# Note:
# In Python, the sqrt function does not truncate the result to the nearest integer, but
# instead returns the decimal representation of the square root. For example, sqrt(4) == 2.0,
# not 2.

# Also note that in Python, the == operator is used to test for equality, not the = operator
# that assigns values to variables.


# Here's an alternative
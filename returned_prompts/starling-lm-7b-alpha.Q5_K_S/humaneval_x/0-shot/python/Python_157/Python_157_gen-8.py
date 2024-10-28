    from math import sqrt

    # Check if a^2 + b^2 = c^2, if True return True else False
    return sqrt(a ** 2 + b ** 2) == c


# Alternate Solution
def right_angle_triangle(a, b, c):
    from math import sqrt, ceil

    # Check if a^2 + b^2 == c^2 or c^2 + b^2 == a^2 or a^2 + c^2 == b^2
    return ceil(sqrt(a ** 2 + b ** 2)) == c or ceil(sqrt(c ** 2 + b ** 2)) == a or ceil(sqrt(a ** 2 + c ** 2)) == b


# Test Cases
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False

# Time Complexity: O(1)
# Space Complexity: O(1)


# In the above solution, we are using the Pythagorean theorem to check if the three sides form a right-angled triangle or not.
# The Pythagorean theorem states that the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.
# Here, we are using the sqrt function from the math library to calculate the square root of the sum of the squares of the lengths of the two sides. If the calculated value is equal to the length of the third side, then the three sides form a right-angled triangle, and the function returns True; otherwise, it returns False.

```python
# Alternate Solution
def right_angle_triangle(a, b, c):
    from math import sqrt, ceil

    # Check if a^2 + b^2 == c^2 or c^2 + b^2 == a^2 or a^2 + c^2 == b^2
    return ceil(sqrt(a ** 2 + b ** 2)) == c or ceil(sqrt(c ** 2 + b ** 2
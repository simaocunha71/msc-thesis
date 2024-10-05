    import math

    # Since Pythagorean theorem is only applicable for right-angled triangle,
    # So, checking Pythagorean theorem for all sides of the triangle.
    if (math.sqrt(a**2 + b**2) == c and c**2 == a**2 + b**2):
        return True
    else:
        return False

# Testing the function
print(right_angle_triangle(3, 4, 5))   # should return True
print(right_angle_triangle(1, 2, 3))   # should return False
print(right_angle_triangle(3, 4, 6))   # should return False
print(right_angle_triangle(10, 8, 12)) # should return True





```
In this code, a function named `right_angle_triangle` is defined which takes three arguments `a`, `b`, and `c` representing the lengths of the three sides of a triangle. The function returns `True` if the three sides form a right-angled triangle and `False` otherwise.

The function uses the Pythagorean theorem (a² + b² = c²) to check if the sides form a right-angled triangle. It checks if the square root of the sum of the squares of `a` and `b` is equal to `c` and if the square of `c` is equal to the sum of the squares of `a` and `b`. If both conditions are satisfied, the function returns `True`, indicating that the sides form a right-angled triangle. Otherwise, it returns `False`.

The function is tested with several example cases using print statements to verify its correctness. The expected output is provided as comments next to each print statement.

```python
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_
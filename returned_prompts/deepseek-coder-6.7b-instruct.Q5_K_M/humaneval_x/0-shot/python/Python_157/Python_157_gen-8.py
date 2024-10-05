
    # First we need to sort the lengths of the sides. This is because the lengths
    # of the sides of a right-angled triangle satisfy the Pythagorean theorem,
    # which states that a^2 + b^2 = c^2. 
    # If a^2 + b^2 > c^2, then c is the longest side and can't be the hypotenuse.
    # If a^2 + b^2 < c^2, then a and b are too small and can't be the sides of
    # a right-angled triangle.
    # So we only need to check that a^2 + b^2 == c^2.

    a, b, c = sorted([a, b, c])

    return a**2 + b**2 == c**2

# Test cases
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle_triangle(7, 24, 25))  # True
print(right_angle_triangle(3, 6, 8))  # False
print(right_angle_triangle(7, 15, 20))  # False
print(right_angle_triangle(3, 3, 3))  # False
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle_triangle(3, 4, 6))  # False
print(right_angle_triangle(7, 24, 25))  # True
print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(7, 15, 20))  # False
print(right_angle_triangle(3, 6, 8))  # False
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle
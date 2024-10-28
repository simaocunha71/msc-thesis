
    # sort the sides of the triangle
    sides = sorted([a, b, c])

    # check if the triangle is a right-angled triangle
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Test cases
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle_triangle(7, 24, 25))  # True
print(right_angle_triangle(3, 6, 8))  # False
print(right_angle_triangle(7, 15, 20))  # False
print(right_angle_triangle(11, 27, 30))  # False
print(right_angle_triangle(9, 15, 22))  # True
print(right_angle_triangle(10, 26, 28))  # True

# Expected Output
# True
# False
# True
# True
# True
# False
# False
# False
# True
# True
"""


def right_angle_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle_triangle(7, 24, 25))  # True
print(right_angle_triangle(3, 6, 8))  # False
print(right_angle_triangle(7, 15,
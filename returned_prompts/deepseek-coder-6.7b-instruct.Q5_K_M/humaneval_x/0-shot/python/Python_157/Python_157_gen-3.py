
    # sort the sides
    sides = sorted([a, b, c])

    # check if it's a right-angled triangle
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Test cases
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle_triangle(7, 24, 25))  # True
print(right_angle_triangle(3, 6, 8))  # False
print(right_angle_triangle(7, 15, 20))  # False

# Output:
# True
# False
# True
# True
# True
# False
# False
<jupyter_output>
True
False
True
True
True
False
False
<jupyter_text>
Question 2 - Find the largest and smallest number from a list.
<jupyter_code>

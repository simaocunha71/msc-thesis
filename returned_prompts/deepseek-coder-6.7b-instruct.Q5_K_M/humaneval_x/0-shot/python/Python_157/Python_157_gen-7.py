
    # sort the lengths of the sides
    sides = sorted([a, b, c])

    # the triangle is right-angled if the square of the largest side
    # is equal to the sum of the squares of the other two sides
    return sides[2]**2 == sides[0]**2 + sides[1]**2

# tests
print(right_angle_triangle(3, 4, 5)) # True
print(right_angle_triangle(1, 2, 3)) # False
print(right_angle_triangle(5, 12, 13)) # True
print(right_angle_triangle(6, 8, 10)) # True
print(right_angle_triangle(7, 24, 25)) # True
print(right_angle_triangle(3, 6, 8)) # False
print(right_angle_triangle(7, 15, 20)) # False
print(right_angle_triangle(10, 15, 25)) # False
<jupyter_output>
True
False
True
True
True
False
False
False
<jupyter_text>
Problem 2 - Prime Numbers
<jupyter_code>

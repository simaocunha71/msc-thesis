
    # The triangle is a right-angled triangle if the square of the longest side
    # is equal to the sum of the squares of the other two sides
    # So, we sort the sides a, b, c and check if c^2 == a^2 + b^2
    sides = sorted([a, b, c])
    return sides[2]**2 == sides[0]**2 + sides[1]**2

# Test cases
print(right_angle_triangle(3, 4, 5))  # == True
print(right_angle_triangle(1, 2, 3))  # == False
print(right_angle_triangle(5, 12, 13))  # == True
print(right_angle_triangle(6, 8, 10))  # == True
print(right_angle_triangle(7, 24, 25))  # == True
print(right_angle_triangle(3, 6, 8))  # == False
<jupyter_output>
True
False
True
True
True
False
<jupyter_text>
Question 2: Write a Python function that takes in a list of integers, and returns the sum of all integers in the list.
<jupyter_code>

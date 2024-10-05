
    # Sorting the lengths of the sides
    sides = sorted([a, b, c])

    # Check if the squares of the two smaller sides sum to the square of the largest side
    return sides[0]**2 + sides[1]**2 == sides[2]**2


# Test cases
print(right_angle_triangle(3, 4, 5)) # True
print(right_angle_triangle(1, 2, 3)) # False
print(right_angle_triangle(5, 12, 13)) # True
print(right_angle_triangle(6, 8, 10)) # True
print(right_angle_triangle(7, 24, 25)) # True
print(right_angle_triangle(3, 6, 8)) # False

# Note: The above function assumes that the inputs are valid and non-negative.
# If the inputs can be negative or non-numeric, you should add error checking to the function.
<jupyter_output>
True
False
True
True
True
False
<jupyter_text>
Question 2
<jupyter_code>

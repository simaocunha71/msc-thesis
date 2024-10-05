
    # The sides of the triangle are a, b, and c. 
    # We know that the triangle is a right-angled triangle if the square of the longest side is 
    # equal to the sum of the squares of the other two sides. 
    # We can use this property to solve the problem.

    if a > b and a > c:
        return a**2 == b**2 + c**2
    elif b > a and b > c:
        return b**2 == a**2 + c**2
    else:
        return c**2 == a**2 + b**2


print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
print(right_angle_triangle(5, 12, 13))  # True
print(right_angle_triangle(6, 8, 10))  # True
print(right_angle_triangle(7, 24, 25))  # True
print(right_angle_triangle(3, 6, 8))  # False
print(right_angle_triangle(7, 15, 20))  # False
print(right_angle_triangle(10, 25, 35))  # False

# This code will print True if the given sides form a right-angled triangle, and False otherwise.
# The function works by first determining which of the three sides is the longest. Then it checks if the square of the longest side is equal to the sum of the squares of the other two sides. If it is, the function returns True, indicating that the three sides form a right-angled triangle. If it isn't, the function returns False.
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
Question 2
<jupyter_code>

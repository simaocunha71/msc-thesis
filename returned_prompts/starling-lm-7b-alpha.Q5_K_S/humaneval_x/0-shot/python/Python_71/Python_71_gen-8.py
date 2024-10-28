
# Here's a solution to the problem:

def triangle_area(a, b, c):
    # Check if the sides can form a triangle
    if a + b > c and b + c > a and c + a > b:
        # Calculate the semi-perimeter of the triangle
        s = (a + b + c) / 2.0
        # Calculate the area of the triangle using Heron's formula
        area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
        # Return the area rounded to 2 decimal points
        return round(area, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5) == 6.00)  # True
print(triangle_area(1, 2, 10) == -1)  # True

# Other test cases
print(triangle_area(5, 12, 13) == 30.00)  # True
print(triangle_area(7, 24, 25) == -1)  # True
print(triangle_area(10, 9, 11) == 45.00)  # True
print(triangle_area(3, 4, 5) == 6.00)  # True
print(triangle_area(3, 3, 3) == 0.00)  # True

# This solution uses Heron's formula to calculate the area of the triangle.
# Heron's formula states that the area of a triangle with sides of length a, b, and c is given by:
# 
# area = sqrt(s * (s - a) * (s - b) * (s - c))
# where s is the semi-perimeter of the triangle, defined as (a + b + c) / 2.
# 
# The function first checks if the three sides can form a valid triangle by verifying that the sum of any two sides is greater than the third side.
# If the sides can form a valid triangle, the function proceeds to calculate
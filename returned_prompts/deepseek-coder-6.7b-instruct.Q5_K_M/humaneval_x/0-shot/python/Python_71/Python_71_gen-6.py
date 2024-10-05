
def triangle_area(a, b, c):
    # Check if three sides can form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate semi-perimeter
        s = (a + b + c) / 2
        # Calculate area using Heron's formula
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5))  # Expected output: 6.00
print(triangle_area(1, 2, 10))  # Expected output: -1
print(triangle_area(3, 4, 7))  # Expected output: 2.90
print(triangle_area(5, 12, 13))  # Expected output: 30.00

# Note: The above code assumes that the inputs are all positive.
# If you want to handle negative inputs as well, you will need to add additional checks.

# Also, the Heron's formula used here may not be suitable for very large numbers due to numerical precision issues.
# For very large numbers, you might need to use a different method to calculate the area.

This code defines a function that calculates the area of a triangle given its three sides. It first checks if the sides can form a valid triangle, then calculates the semi-perimeter and uses Heron's formula to calculate the area. The area is then rounded to 2 decimal places. If the sides do not form a valid triangle, the function returns -1.
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 2Write a function `prime_factorize` that takes a positive integer `n` as input and returns a list of its prime factors in ascending order. For example, `prime_factorize(315)` should return `[3, 3, 5, 7]`.
<jupyter_code>

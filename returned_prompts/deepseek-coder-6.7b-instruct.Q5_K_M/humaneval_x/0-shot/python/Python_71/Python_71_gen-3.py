
    # check if the three sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1

print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1

This function first checks if the given sides can form a valid triangle. If not, it immediately returns -1. If the sides can form a valid triangle, the function calculates the semi-perimeter of the triangle, and then uses Heron's formula to calculate the area. The area is then rounded to two decimal points using the built-in round function and returned.

Here is a simple test of the function:

print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1

The first test should return 6.00, and the second test should return -1.

This function should work correctly for all valid triangle sides lengths. If you pass in invalid values (such as negative numbers or non-numeric values), it may not behave as expected.

It's a good idea to add some error checking at the beginning of the function to make sure the inputs are valid.

def triangle_area(a, b, c):
    if not all(isinstance(i, (int, float)) for i in (a, b, c)) or a <= 0 or b <= 0 or c <= 0:
        return -1
    # rest of function...

This version of the function will return -1 if any of the inputs are not numbers or if any of the numbers are less than or equal to 0.

This is just a simple example of how you might add error checking to the function. In a real-world program, you would probably want to add more checks
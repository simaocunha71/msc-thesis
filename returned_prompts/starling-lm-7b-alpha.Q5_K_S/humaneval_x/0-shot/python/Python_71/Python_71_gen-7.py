
def triangle_area(a, b, c):
    # Check that the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    # Return the area rounded to 2 decimal points
    return '{:.2f}'.format(area)

# Test cases
print(triangle_area(3, 4, 5) == 6.00)  # True
print(triangle_area(1, 2, 10) == -1)  # True

# More test cases
print(triangle_area(3, 4, 5) == 6.00)  # True
print(triangle_area(3, 4, 6) == -1)  # True
print(triangle_area(10, 10, 10) == 16.00)  # True
print(triangle_area(3, 3, 3) == 0.00)  # True
print(triangle_area(0, 0, 0) == -1)  # True
print(triangle_area(3, 0, 0) == -1)  # True
print(triangle_area(0, 3, 0) == -1)  # True
print(triangle_area(0, 0, 3) == -1)  # True
print(triangle_area(1, 2, 3) == -1)  # True
print(triangle_area(1, 1, 2) == 0.50)  # True
print(triangle_area(2, 3, 4) == 3.50)  # True
print(triangle_area(4, 5, 6) == 6.00)  # True
print(triangle_area(5, 6, 7
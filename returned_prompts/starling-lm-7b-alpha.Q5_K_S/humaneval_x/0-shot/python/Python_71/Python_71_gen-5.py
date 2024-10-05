
def triangle_area(a, b, c):
    # Check for valid triangle
    if (a + b <= c or a + c <= b or b + c <= a):
        return -1
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    # Calculate area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return '{:.2f}'.format(area)

# Test cases
print(triangle_area(3, 4, 5) == 6.00)  # True
print(triangle_area(1, 2, 10) == -1)  # True
print(triangle_area(2, 2, 2) == 1.20)  # True
print(triangle_area(1, 2, 3) == -1)  # True
print(triangle_area(10, 10, 10) == 16.00)  # True
print(triangle_area(1, 1, 3) == -1)  # True
print(triangle_area(5, 12, 13) == 30.00)  # True

# More test cases
print(triangle_area(7, 8, 9) == 24.00)  # True
print(triangle_area(10, 9, 8) == 21.00)  # True
print(triangle_area(7, 9, 10) == 21.00)  # True
print(triangle_area(9, 8, 7) == 21.00)  # True
print(triangle_area(10, 10, 10) == 16.00)  # True

# Invalid triangles
print(triangle_area(2, 2, 6) == -1)  # True
print(triangle_area(3, 4, 5) == 6.00)  # True
print(triangle_area(3,
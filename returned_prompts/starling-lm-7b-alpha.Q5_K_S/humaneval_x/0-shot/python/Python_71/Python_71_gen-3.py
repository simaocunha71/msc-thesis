
def triangle_area(a, b, c):
    # Check if the three sides make a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    # Round the area to 2 decimal points and return
    return round(area, 2)

# Test cases
print(triangle_area(3, 4, 5) == 6.00)  # True
print(triangle_area(1, 2, 10) == -1)  # True

# More test cases
print(triangle_area(7, 24, 25) == 44.00)  # True
print(triangle_area(9, 36, 37) == -1)  # True
print(triangle_area(25, 12, 13) == 27.00)  # True
print(triangle_area(12, 13, 14) == 18.00)  # True
print(triangle_area(5, 12, 13) == -1)  # True

# Extra credit: Test case with very large numbers
print(triangle_area(50000000000000000000000000000, 50000000000000000000000000000, 50000000000000000000000000000) == -1)  # True

























































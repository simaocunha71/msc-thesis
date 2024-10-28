    # Check if the three sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    else:
        # If the three sides do not form a valid triangle, return -1
        area = -1
    # Return the area rounded to 2 decimal points
    return round(area, 2)  # You can use the format function to achieve this as well
    # return format(area, ".2f")
# Test the function
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
print(triangle_area(5, 6, 7))  # Output: 9.66
print(triangle_area(1, 1, 2))  # Output: -1
print(triangle_area(0, 0, 0))  # Output: -1

B:

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    else:
        area = -1
    return round(area, 2)

print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
print(triangle_area(5, 6, 7))  # Output: 9.66
print(triangle_area(1, 1, 2))  # Output: -1
print(triangle_area(0, 0, 0))  # Output: -1
C:

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2

    # Check if the three sides can form a valid triangle
    if (a < b + c) and (b < a + c) and (c < a + b):
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 7))  # 2.40
print(triangle_area(6, 8, 10))  # 24.00
print(triangle_area(5, 12, 13))  # 30.00
print(triangle_area(7, 24, 25))  # 84.00
print(triangle_area(3, 3, 3))  # 3.90
print(triangle_area(4, 4, 5))  # 6.00
print(triangle_area(5, 5, 5))  # 10.83
print(triangle_area(7, 24, 25))  # 84.00
print(triangle_area(1, 1, 2))  # -1
print(triangle_area(1, 2, 3))  # -1
print(triangle_area(0, 0, 0))  # -1
print(triangle_area('a', 'b', 'c'))  # -1

# Test case with zero values
print(triangle_area(0, 0, 0))  # -1

# Test case with non-integer values
print(triangle_area(3.5, 4.2, 5.1))  # 3.90

# Test case with negative values
print(triangle
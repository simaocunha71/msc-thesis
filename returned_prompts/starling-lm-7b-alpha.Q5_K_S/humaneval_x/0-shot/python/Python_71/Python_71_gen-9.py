
def triangle_area(a, b, c):
    # Check if triangle is valid
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        return -1
    # Calculate the semi-perimeter
    s = (a + b + c)/2
    # Calculate the area
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    # Round the area to 2 decimal points
    return round(area, 2)

# Tests
print(round(triangle_area(3, 4, 5), 2) == 6.00) # True
print(round(triangle_area(1, 2, 10), 2) == -1) # True




def triangle_area(a, b, c):
    if not (a + b > c) and not (b + c > a) and not (c + a > b):
        return -1
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


# Tests
print(round(triangle_area(3, 4, 5), 2) == 6.00)  # True
print(round(triangle_area(1, 2, 10), 2) == -1)  # True



# Here is the Python 3 solution:
def triangle_area(a, b, c):
    if (not (a + b > c)) and (not (b + c > a)) and (not (c + a > b)):
        return -1
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Tests
print(round(triangle_area(3, 4, 5), 2) == 6.00)  # True
print(round(triangle_area(1, 2, 10), 2) == -1)  #
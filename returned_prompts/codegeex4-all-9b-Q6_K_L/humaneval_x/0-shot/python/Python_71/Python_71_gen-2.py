def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # Check if the given sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Calculate the area of the triangle using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # Round the area to 2 decimal points
    area = round(area, 2)

    return area

print(triangle_area(3, 4, 5))  # Output: 6.0
print(triangle_area(1, 2, 10))  # Output: -1
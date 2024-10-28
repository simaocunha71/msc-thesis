    import math

    # Check if the three sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Round the area to 2 decimal points
    area = round(area, 2)

    return area


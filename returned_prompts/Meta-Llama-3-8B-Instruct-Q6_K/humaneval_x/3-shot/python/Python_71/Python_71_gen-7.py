    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Check if the three sides form a valid triangle
    if s < a or s < b or s < c:
        return -1

    # Calculate the area of the triangle
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # Round the area to 2 decimal points
    return round(area, 2)



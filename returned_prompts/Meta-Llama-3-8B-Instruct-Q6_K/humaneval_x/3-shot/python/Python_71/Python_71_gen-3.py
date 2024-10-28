    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Check if the three sides form a valid triangle
    if s > a and s > b and s > c:
        # Calculate the area of the triangle
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1



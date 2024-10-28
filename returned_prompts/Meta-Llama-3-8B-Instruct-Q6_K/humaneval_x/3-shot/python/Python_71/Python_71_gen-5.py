    # Check if the three sides can form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        # Round the area to 2 decimal points
        area = round(area, 2)
        return area
    else:
        return -1



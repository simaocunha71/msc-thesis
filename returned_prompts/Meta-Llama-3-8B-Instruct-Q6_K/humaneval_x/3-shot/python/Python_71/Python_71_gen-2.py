    import math

    # Check if the three sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # Return the area rounded to 2 decimal points
        return round(area, 2)
    else:
        # Return -1 if the three sides do not form a valid triangle
        return -1



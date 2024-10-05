    if a + b > c and a + c > b and b + c > a:
        # Calculate semi-perimeter
        s = (a + b + c) / 2
        # Calculate area using Heron's formula
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1



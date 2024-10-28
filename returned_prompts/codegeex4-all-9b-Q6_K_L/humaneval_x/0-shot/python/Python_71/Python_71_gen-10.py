def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return round((a * b * c) / (4 * ((a + b + c) / 2) * ((a + b - c) / 2) * ((b + c - a) / 2) * ((c + a - b) / 2)), 2)
    else:
        return -1
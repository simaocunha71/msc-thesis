
def triangle_area(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        return -1
    else:
        s = (a + b + c) / 2
        return round(s * (s - a) * (s - b) * (s - c), 2)

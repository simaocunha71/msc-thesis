
def triangle_area(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        s = (a + b + c) / 2
        return round(2 * (s * (s - a) * (s - b) * (s - c)), 2)
    else:
        return -1



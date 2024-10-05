    def is_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    if is_triangle(a, b, c):
        s = (a + b + c) / 2
        return round(s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1



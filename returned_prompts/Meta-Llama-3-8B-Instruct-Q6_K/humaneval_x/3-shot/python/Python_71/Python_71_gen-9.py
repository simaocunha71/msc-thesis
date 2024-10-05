    def calculate_perimeter(a, b, c):
        return a + b + c

    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    if is_valid_triangle(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1



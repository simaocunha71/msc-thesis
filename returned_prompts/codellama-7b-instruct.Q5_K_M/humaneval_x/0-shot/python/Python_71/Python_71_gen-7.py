
def triangle_area(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return -1
    return (a * b * c) ** 0.5 / 2

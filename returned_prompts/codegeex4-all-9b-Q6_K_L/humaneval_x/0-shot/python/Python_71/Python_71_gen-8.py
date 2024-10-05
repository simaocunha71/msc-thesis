def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return round(area, 2)

print(triangle_area(3, 4, 5))  # 6.0
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(5, 6, 8))  # 16.0
print(triangle_area(3, 3, 3))  # 3.8971143170299746
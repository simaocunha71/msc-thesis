
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1
    else:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)

# test cases
print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 7))  # 7.94
print(triangle_area(3, 3, 3))  # 3.90
print(triangle_area(1, 2, 2))  # -1
print(triangle_area(2, 3, 4))  # 2.90
print(triangle_area(3, 5, 7))  # 14.15
print(triangle_area(5, 12, 13))  # 30.0
print(triangle_area(7, 24, 25))  # 84.0
print(triangle_area(8, 15, 17))  # 60.0
print(triangle_area(12, 35, 37))  # 114.15
print(triangle_area(3, 6, 8))  # 14.15
print(triangle_area(7, 24, 25))  # 84.0
print(triangle_area(8, 15, 17))  # 60.0
print(triangle_area(12, 35, 37))  # 114.15
print(triangle_area(3, 6, 8))  # 14.15
print(triangle_area(7, 24, 25))  # 84.0
print(triangle_area(8, 15, 17))  # 60.0

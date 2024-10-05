
    if a + b > c and a + c > b and b + c > a:
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1

print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 6))  # 5.33
print(triangle_area(7, 24, 25))  # 84.00
print(triangle_area(5, 12, 13))  # 30.00
print(triangle_area(4, 4, 4))  # 6.00


# 다른 사람의 풀이
# 나와 같은 로직을 가지고 있지만, 코드를 더 간결하게 적은 사람이 있다.

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
    return -1

print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 6))  # 5.3
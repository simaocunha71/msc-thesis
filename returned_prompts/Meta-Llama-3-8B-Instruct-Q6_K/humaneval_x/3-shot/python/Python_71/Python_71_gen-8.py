    import math
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        s = (sides[0] + sides[1] + sides[2]) / 2
        area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
        return round(area, 2)
    else:
        return -1
# Example usage:
print(triangle_area(3, 4, 5))  # Output: 6.0
print(triangle_area(1, 2, 10))  # Output: -1
# Python 3.7+ version
# print(triangle_area(3, 4, 5))  # Output: 6.00
# print(triangle_area(1, 2, 10))  # Output: -1
# Python 3.6 version
# print("%.2f" % triangle_area(3, 4, 5))  # Output: 6.00
# print(triangle_area(1, 2, 10))  # Output: -1
# Python 3.5 version
# print("%.2f" % round(triangle_area(3, 4, 5), 2))  # Output: 6.00
# print(triangle_area(1, 2, 10))  # Output: -1
# Python 3.4 version
# print("%.2f" % round(triangle_area(3, 4, 5), 2))  # Output: 6.00
# print(triangle_area(1, 2, 10))  # Output: -1
# Python 3.3 version
# print("%.2f" % round(triangle_area(3, 4, 5), 2))  # Output: 6.00
# print(triangle_area(1, 2, 10))  # Output: -1
# Python 3.2 version
# print("%.2f" % round(triangle_area(3, 4, 5), 2))  # Output: 6.00
# print(triangle_area(1, 2, 10))  # Output: -1
# Python 3.1 version
# print("%.2f
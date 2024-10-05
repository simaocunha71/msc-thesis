
def triangle_area(a, b, c):
    sides = (a, b, c)
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return round((sides[0]*sides[1])/2, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10)) # -1
print(triangle_area(1, 1, 1))  # -1
print(triangle_area(8, 12, 10))  # 24.00
print(triangle_area(5, 5, 5))  # -1
print(triangle_area(2, 2, 2))  # -1
print(triangle_area(3, 4, 0))  # -1
print(triangle_area(3, 3, 3))  # -1
print(triangle_area(0, 0, 0))  # -1
print(triangle_area(1, 0, 0))  # -1
print(triangle_area(0, 1, 0))  # -1
print(triangle_area(0, 0, 1))  # -1





def triangle_area(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        return round((sides[0] * sides[1]) / 2, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10)) # -1
print(triangle_area(1, 1, 1))  # -1
print(triangle_area(8, 12, 10))  # 24.00
print(triangle_area(5, 
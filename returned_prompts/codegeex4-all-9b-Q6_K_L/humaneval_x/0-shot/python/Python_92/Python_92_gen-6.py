def any_int(x, y, z):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        return False
    return x == y + z or y == x + z or z == x + y

print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))
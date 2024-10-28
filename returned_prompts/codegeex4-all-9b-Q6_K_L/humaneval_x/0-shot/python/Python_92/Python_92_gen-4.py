def any_int(x, y, z):
    return any(map(lambda x: x.is_integer(), (x, y, z))) and (x + y == z or x + z == y or y + z == x)

print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))
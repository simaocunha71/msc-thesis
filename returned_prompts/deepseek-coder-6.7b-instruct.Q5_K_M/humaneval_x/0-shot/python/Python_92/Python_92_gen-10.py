
def any_int(x, y, z):
    if not all(isinstance(i, int) for i in (x, y, z)):
        return False
    return any(i == x + y for i in (z,)) or any(i == x + z for i in (y,)) or any(i == y + z for i in (x,))

print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))



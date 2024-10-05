def any_int(x, y, z):
    if all(isinstance(i, int) for i in [x, y, z]):
        return x + y == z or y + z == x or z + x == y
    else:
        return False

print(any_int(5, 2, 7)) #➞ True
print(any_int(3, 2, 2)) #➞ False
print(any_int(3, -2, 1)) #➞ True
print(any_int(3.6, -2.2, 2)) #➞ False

def any_int(x, y, z):
    if x == int(x) and y == int(y) and z == int(z):
        return x == y + z or y == x + z or z == x + y
    return False

print(any_int(5, 2, 7)) # ➞ True
print(any_int(3, 2, 2)) # ➞ False
print(any_int(3, -2, 1)) # ➞ True
print(any_int(3.6, -2.2, 2)) # ➞ False
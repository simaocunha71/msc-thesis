
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return x == y + z or y == x + z or z == x + y

print(any_int(5, 2, 7)) # ➞ True

print(any_int(3, 2, 2)) # ➞ False

print(any_int(3, -2, 1)) # ➞ True

print(any_int(3.6, -2.2, 2)) # ➞ False

print(any_int(3, 2, 5)) # ➞ False

print(any_int(0, 0, 0)) # ➞ True

print(any_int(-1, -1, -2)) # ➞ True

print(any_int(1, 2, 3)) # ➞ False

print(any_int(1, 1, 1)) # ➞ True

print(any_int(10, 20, 30)) # ➞ False

print(any_int(-10, -20, -30)) # ➞ False

print(any_int(-10, 20, 20)) # ➞ True

print(any_int(10, -20, -10)) # ➞ True

print(any_int(1, 2, 0)) # ➞ True

print(any_int(0, 0, 1)) # ➞ True

print(any_int(0, 1, 1)) # ➞ True

print(any_int(1, 0, 1)) # ➞ True

print(any_int(1, 1, 2)) # ➞ True

print(any_int(1, 2, 0)) # ➞ True

print(any_int(2, 1,
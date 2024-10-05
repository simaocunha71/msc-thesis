
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return x == y + z or y == x + z or z == x + y
    return False

print(any_int(5, 2, 7)) # ➞ True

print(any_int(3, 2, 2)) # ➞ False

print(any_int(3, -2, 1)) # ➞ True

print(any_int(3.6, -2.2, 2)) # ➞ False

print(any_int(3, 2, 5)) # ➞ True

print(any_int(3, 2, 1)) # ➞ False

print(any_int(-3, 2, 5)) # ➞ True

print(any_int(3, 0, 5)) # ➞ True

print(any_int(3, 2, -2)) # ➞ True

print(any_int(3, 2, 0)) # ➞ True

print(any_int(0, 2, 2)) # ➞ True

print(any_int(1, 1, 1)) # ➞ True

print(any_int(1, 2, 3)) # ➞ False

print(any_int(-1, -2, -3)) # ➞ True

print(any_int(-1, -2, 3)) # ➞ True

print(any_int(-1, 2, 3)) # ➞ True

print(any_int(1, 0, 0)) # ➞ True

print(any_int(0, 0, 0)) # ➞ True
<jupyter_output>
True
False
True
False
True
False
True
True
True
True
True
True
True
True
True
True
True
True
True
True

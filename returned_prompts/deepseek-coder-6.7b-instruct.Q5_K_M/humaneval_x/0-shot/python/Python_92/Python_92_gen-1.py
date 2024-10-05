
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == y + z or y == x + z or z == x + y:
            return True
    return False

print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))

print(any_int(2, 2, 2))
print(any_int(3, -2, 1.5))
print(any_int(3, -2, 2))
print(any_int(5, 2, 3))
<jupyter_output>
True
False
True
False
True
False
False
False
<jupyter_text>

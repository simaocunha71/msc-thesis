
def any_int(x, y, z):
    if x == y + z and isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return True
    else:
        return False

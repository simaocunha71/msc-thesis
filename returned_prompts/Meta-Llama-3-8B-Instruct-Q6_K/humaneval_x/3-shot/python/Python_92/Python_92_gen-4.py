    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return x + y == z or x + z == y or y + z == x
    else:
        return False



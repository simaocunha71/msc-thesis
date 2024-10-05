    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == y + z or x + y == z or x + z == y:
            return True
    return False



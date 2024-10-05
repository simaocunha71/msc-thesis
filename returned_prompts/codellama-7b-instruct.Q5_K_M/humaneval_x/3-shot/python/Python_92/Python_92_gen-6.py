    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        return False
    if x == y + z:
        return True
    if y == x + z:
        return True
    if z == x + y:
        return True
    return False




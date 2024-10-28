def any_int(x, y, z):
    return all(isinstance(i, int) for i in (x, y, z)) and (x == y + z or y == x + z or z == x + y)
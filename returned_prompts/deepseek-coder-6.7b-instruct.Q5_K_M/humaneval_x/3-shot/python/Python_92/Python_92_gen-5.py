    return any(x+y == z and all(isinstance(i, int) for i in (x, y, z)) for z in (x, y, z))


    def any_int(x, y, z):
        if x + y == z or x + z == y or y + z == x:
            if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
                return True
        return False
    return any_int(x, y, z)



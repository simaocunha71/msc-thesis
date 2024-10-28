    def any_int(x, y, z):
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
            return False
        if x + y == z or x + z == y or y + z == x:
            return True
        return False

    return any_int(x, y, z)



    def any_int(x, y, z):
        if type(x) is int and type(y) is int and type(z) is int:
            return (x + y) == z or (x + z) == y or (y + z) == x
        else:
            return False



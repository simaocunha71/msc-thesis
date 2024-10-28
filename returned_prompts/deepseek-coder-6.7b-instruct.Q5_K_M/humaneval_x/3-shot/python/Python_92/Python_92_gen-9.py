    def any_int(x, y, z):
        return (int(x)+int(y) == int(z) or int(x)+int(z) == int(y) or int(y)+int(z) == int(x)) and isinstance(x, int) and isinstance(y, int) and isinstance(z, int)



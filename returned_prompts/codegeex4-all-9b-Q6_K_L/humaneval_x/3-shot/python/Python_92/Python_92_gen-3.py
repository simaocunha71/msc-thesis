    def is_integer(n):
        return n.is_integer()

    if is_integer(x) and is_integer(y) and is_integer(z):
        return x == y + z or y == x + z or z == x + y
    else:
        return False


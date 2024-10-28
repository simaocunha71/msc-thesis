    def is_integer(n):
        return n.is_integer()

    if is_integer(x) and is_integer(y) and is_integer(z):
        if x + y == z or x + z == y or y + z == x:
            return True
    return False


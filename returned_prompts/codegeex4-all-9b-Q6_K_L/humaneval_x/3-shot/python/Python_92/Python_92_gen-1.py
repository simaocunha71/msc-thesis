    def is_integer(n):
        return n.is_integer()

    if is_integer(x) and is_integer(y) and is_integer(z):
        if x + y == z or y + z == x or x + z == y:
            return True
        else:
            return False
    else:
        return False


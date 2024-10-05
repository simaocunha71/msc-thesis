    def is_integer(num):
        return num.is_integer()

    if is_integer(x) and is_integer(y) and is_integer(z):
        if x == y + z or y == x + z or z == x + y:
            return True
        else:
            return False
    else:
        return False


    if type(x) == int and type(y) == int and type(z) == int and (x == y + z or y == z + x or z == x + y):
        return True
    else:
        return False



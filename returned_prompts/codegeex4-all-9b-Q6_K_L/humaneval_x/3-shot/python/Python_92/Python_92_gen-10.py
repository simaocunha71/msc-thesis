    if type(x) == int and type(y) == int and type(z) == int:
        if x + y == z or x + z == y or y + z == x:
            return True
        else:
            return False
    else:
        return False


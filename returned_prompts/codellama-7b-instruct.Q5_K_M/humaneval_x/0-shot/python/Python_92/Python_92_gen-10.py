
def any_int(x, y, z):
    if type(x) != int or type(y) != int or type(z) != int:
        return False
    if x == y + z:
        return True
    else:
        return False

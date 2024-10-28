    def any_int(x, y, z):
        if int(x) == (int(y) + int(z)):
            return True
        elif int(y) == (int(x) + int(z)):
            return True
        elif int(z) == (int(x) + int(y)):
            return True
        else:
            return False
    return any_int(x, y, z)



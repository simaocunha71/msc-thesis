    if x > y or (x % 2 != 0 and y % 2 != 0):
        return -1
    elif x == y:
        return x
    elif x % 2 != 0:
        return x
    elif y % 2 == 0:
        return y
    else:
        return y - 1



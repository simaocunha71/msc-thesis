    if x % 2 == 0:
        if y % 2 == 0:
            return y
        else:
            return x
    elif y % 2 == 0:
        return y
    else:
        return -1



    if y == 0 or y == 1:
        return -1

    if x % 2 == 0:
        if x <= y:
            return x
        else:
            return x - 2
    else:
        if x <= y:
            return x - 1
        else:
            return x - 2



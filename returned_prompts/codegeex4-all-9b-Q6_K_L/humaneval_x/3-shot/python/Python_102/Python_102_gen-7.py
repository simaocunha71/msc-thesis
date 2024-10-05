    if x > y or x < 0 or y < 0:
        return -1

    if x % 2 == 0:
        return x
    elif x + 1 > y:
        return -1
    else:
        return x + 1


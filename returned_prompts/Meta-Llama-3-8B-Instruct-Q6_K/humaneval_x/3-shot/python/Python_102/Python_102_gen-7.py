    if x % 2 == 0 and y % 2 == 0:
        return min(x, y)
    elif x % 2 == 0:
        return x
    elif y % 2 == 0:
        return y
    else:
        return -1

    if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
        return max(x, y) - 1
    elif x % 2 == 1 and y % 2 == 0:
        return y
    else:
        return -1



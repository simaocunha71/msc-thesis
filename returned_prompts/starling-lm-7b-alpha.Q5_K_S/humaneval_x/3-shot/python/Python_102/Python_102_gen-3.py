    if x % 2 == 0 and x <= y and y % 2 == 0:
        return y
    elif x % 2 == 0 and x <= y and y % 2 != 0:
        return x
    elif x % 2 != 0 and x <= y and y % 2 == 0:
        return y - 1
    elif x % 2 != 0 and x <= y and y % 2 != 0:
        return x
    elif x % 2 == 0 and x > y and y % 2 == 0:
        return y
    elif x % 2 == 0 and x > y and y % 2 != 0:
        return x - 1
    elif x % 2 != 0 and x > y and y % 2 == 0:
        return y - 1
    elif x % 2 != 0 and x > y and y % 2 != 0:
        return x - 1
    else:
        return -1



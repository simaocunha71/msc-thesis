
def choose_num(x, y):
    if x == y:
        if x % 2 == 0:
            return x
        else:
            return -1
    if x > y:
        if y % 2 == 0:
            return y
        else:
            return -1
    if x < y:
        if x % 2 == 0:
            return x
        else:
            if (y - 1) % 2 == 0:
                return y - 1
            else:
                return -1

choose_num(12, 15) # returns: 14
choose_num(13, 12) # returns: -1


# Another solution
def choose_num(x, y):
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i
    return -1


# Another solution
def choose_num(x, y):
    if x % 2 == 0:
        return x
    if y % 2 == 0:
        return y
    if (y-1) % 2 == 0:
        return y-1
    return -1

# Another solution
def choose_num(x, y):
    return -1 if x % 2 != 0 and y % 2 != 0 else max(x, y) if x <= y else max(x, y) - 1 if y % 2 == 0 else -1


# Another solution
def choose_num(x, y):
    if x % 2 == 0:
        return x
    if y % 2 == 0:
        return y
    if (y - 1) % 2 == 0:
        return y - 1
    return -1


# Another solution
def choose_num(x, y):
    if x % 2 == 0:
        return x
    elif y % 2 == 0:
        return y
    elif (y-1) % 2 == 0:
        return y-1
    else:
        return -1


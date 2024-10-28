    if a == 0:
        return b
    if b == 0:
        return a

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a



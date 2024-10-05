    if x <= 0:
        return False

    power = 1
    while power < x:
        power *= n

    return power == x


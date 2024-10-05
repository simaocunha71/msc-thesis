    if x < 1:
        return False

    power = 1
    while power < x:
        power *= n

    return power == x


    if x == 1 or x == 0:
        return True
    base = 2
    while base <= x:
        power = 1
        while base ** power < x:
            power += 1
        if base ** power == x:
            return True
        base += 1
    return False



    if not arr:
        return None

    prod = 1
    for x in arr:
        if x < 0:
            prod *= -1
        elif x > 0:
            prod *= 1
        else:
            prod *= 0

    return sum(abs(x) for x in arr) * prod



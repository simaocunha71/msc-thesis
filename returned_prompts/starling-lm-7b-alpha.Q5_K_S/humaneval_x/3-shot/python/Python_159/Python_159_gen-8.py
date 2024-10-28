    if remaining < need - number:
        return [number + remaining, 0]
    else:
        return [need + number, remaining - need + number]



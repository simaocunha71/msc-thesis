    if number + remaining < need:
        return [number + remaining, 0]
    else:
        return [number + remaining, need - number]



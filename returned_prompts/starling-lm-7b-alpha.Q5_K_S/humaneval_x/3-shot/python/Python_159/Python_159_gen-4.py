    if remaining < need:
        return [number + remaining, 0]
    else:
        return [number + need, remaining - need]



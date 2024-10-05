    if need > remaining:
        return [remaining + number, 0]
    else:
        return [need + number, remaining - need]
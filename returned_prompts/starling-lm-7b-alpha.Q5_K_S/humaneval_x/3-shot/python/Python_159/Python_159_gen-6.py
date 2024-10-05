    total = number + need
    left = remaining - (need - total)
    if left < 0:
        left = 0
    return [total, left]



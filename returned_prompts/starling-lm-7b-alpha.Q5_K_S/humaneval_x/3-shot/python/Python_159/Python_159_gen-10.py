    if remaining + number >= need:
        total = number + remaining + need
        left = remaining - (need - number)
    else:
        total = number + remaining
        left = 0
    return [total, left]



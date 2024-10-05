    if remaining >= need - number:
        total_eaten = number + need
        remaining = remaining - need + number
    else:
        total_eaten = number + remaining
        remaining = 0

    return [total_eaten, remaining]



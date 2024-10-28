    eat_all = need - remaining
    if eat_all > 0:
        return [number + remaining, 0]
    else:
        return [number + need, remaining + eat_all]



    if not arr:
        return None

    prod = 1
    for n in arr:
        prod *= (1 if n > 0 else -1 if n < 0 else 0)

    return sum(abs(n) for n in arr) * prod



    if n < 2:
        return []
    else:
        return [x for x in range(2, n) if all(x % y for y in range(2, int(x ** 0.5) + 1))]



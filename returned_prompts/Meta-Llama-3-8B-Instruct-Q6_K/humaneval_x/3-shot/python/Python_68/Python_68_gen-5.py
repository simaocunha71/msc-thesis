    if not arr:
        return []
    evens = [(x, i) for i, x in enumerate(arr) if x % 2 == 0]
    if not evens:
        return []
    return min(evens, key=lambda x: (x[0], x[1]))



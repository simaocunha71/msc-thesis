    if len(l) <= 1:
        return True
    if l[1] < l[0]:
        return all(x >= y for x, y in zip(l, l[1:]))
    if l[1] > l[0]:
        return all(x <= y for x, y in zip(l, l[1:]))
    return True



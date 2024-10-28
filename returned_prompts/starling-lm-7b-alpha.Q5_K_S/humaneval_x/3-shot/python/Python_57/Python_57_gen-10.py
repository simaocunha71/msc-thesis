    return all(a <= b for a, b in zip(l, l[1:])) or all(a >= b for a, b in zip(l, l[1:]))



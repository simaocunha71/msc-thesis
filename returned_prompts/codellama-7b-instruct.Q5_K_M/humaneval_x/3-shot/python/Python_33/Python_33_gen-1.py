    return [x for i, x in enumerate(l) if i % 3 != 0] + sorted([x for i, x in enumerate(l) if i % 3 == 0])



    return [x if i % 2 != 0 else sorted([x for x in l if i % 2 == 0])[0] for i, x in enumerate(l)]



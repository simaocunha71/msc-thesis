    return [x if i % 2 != 0 else sorted([y for y in l if i % 2 == 0])[0] for i, x in enumerate(l)]



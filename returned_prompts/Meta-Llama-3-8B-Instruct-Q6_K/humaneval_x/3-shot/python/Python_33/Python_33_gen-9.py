    return [x if i % 3 != 0 else sorted([y for y in l if i % 3 == 0])[0] for i, x in enumerate(l)]



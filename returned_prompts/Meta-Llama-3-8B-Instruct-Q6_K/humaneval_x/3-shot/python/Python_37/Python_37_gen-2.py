    return [x if i % 2 else sorted([y for y in l if i == (l.index(y))])[0] for i, x in enumerate(l)]



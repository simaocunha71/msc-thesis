    return [x if i % 2 else sorted([y for y in l if i == (j + 1) % 2])[0] for i, x in enumerate(l)]



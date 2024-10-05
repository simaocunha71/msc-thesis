    return [x if i % 2 != 0 else sorted([y for y in l if i == 2 * j + 1])[j] for i, x in enumerate(l)]



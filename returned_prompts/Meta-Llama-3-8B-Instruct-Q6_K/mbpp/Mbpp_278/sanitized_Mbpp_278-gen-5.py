def count_first_elements(t):
    return sum(1 for x in t if isinstance(x, tuple) or x in t[:t.index((x for y in t if isinstance(y, tuple))[0]) + 1]) - 1
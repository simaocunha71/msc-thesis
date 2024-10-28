def interleave_lists(a, b, c):
    return [val for pair in zip(a, b, c) for val in pair]
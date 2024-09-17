def extract_singly(t):
    return reduce(lambda x, y: x + y, map(lambda x: x[0], t))
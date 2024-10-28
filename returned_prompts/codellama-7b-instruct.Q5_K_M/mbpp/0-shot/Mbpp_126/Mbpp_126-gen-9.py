def sum(a, b):
    return sum(set(range(1, min(a, b) + 1)) & set(range(1, max(a, b) + 1)))

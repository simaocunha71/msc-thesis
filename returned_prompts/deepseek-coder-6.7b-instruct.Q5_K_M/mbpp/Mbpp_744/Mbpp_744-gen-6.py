def check_none(t):
    return any(x is None for x in t)

print(check_none((10, 4, 5, 6, None)))  # True



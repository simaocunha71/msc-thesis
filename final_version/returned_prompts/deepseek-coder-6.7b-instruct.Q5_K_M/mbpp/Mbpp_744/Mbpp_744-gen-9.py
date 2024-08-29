
def check_none(tup):
    return any(x is None for x in tup)

print(check_none((10, 4, 5, 6, None)))  # True


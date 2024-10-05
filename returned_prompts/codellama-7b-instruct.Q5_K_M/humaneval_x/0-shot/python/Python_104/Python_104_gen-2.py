
def unique_digits(x):
    return sorted(filter(lambda y: not any(map(lambda z: z % 2 == 0, str(y))), x))
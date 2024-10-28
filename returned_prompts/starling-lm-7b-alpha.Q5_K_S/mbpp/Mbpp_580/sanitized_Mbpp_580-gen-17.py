def extract_even(t):
    return tuple(filter(lambda x: len(str(x)) % 2 == 0, t))
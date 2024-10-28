def multiply_elements(tup):
    return tuple(a * b for a, b in zip(tup[:-1], tup[1:]))
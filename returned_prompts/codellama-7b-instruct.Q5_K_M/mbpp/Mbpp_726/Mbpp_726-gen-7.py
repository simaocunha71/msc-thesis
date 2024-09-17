
def multiply_elements(tup):
    return tuple(a * b for a, b in zip(tup, tup[1:]))



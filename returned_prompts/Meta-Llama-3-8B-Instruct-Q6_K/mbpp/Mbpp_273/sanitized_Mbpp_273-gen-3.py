def substract_elements(tup1, tup2):
    return tuple(x - y for x, y in zip(tup1, tup2)) if len(tup1) == len(tup2) else "Tuples must be of the same length"
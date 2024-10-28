def substract_elements(tup1, tup2):
    if len(tup1) != len(tup2):
        raise ValueError("Tuples should have the same length")
    return tuple(map(lambda x, y: x - y, tup1, tup2))

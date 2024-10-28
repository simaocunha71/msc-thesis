def division_elements(tup1, tup2):
    if len(tup1) != len(tup2):
        raise ValueError("Both tuples should have the same length")
    return tuple(x / y for x, y in zip(tup1, tup2))
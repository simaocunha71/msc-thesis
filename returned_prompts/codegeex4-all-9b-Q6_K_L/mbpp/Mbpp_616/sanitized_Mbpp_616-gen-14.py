def tuple_modulo(tup1, tup2):
    if len(tup1) != len(tup2):
        raise ValueError("Tuples must be of the same length")
    return tuple(a % b for a, b in zip(tup1, tup2))
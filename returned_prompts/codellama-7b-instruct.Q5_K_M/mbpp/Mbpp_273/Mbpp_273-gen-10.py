def substract_elements(tuple_1, tuple_2):
    if len(tuple_1) != len(tuple_2):
        raise ValueError("Both tuples must have the same length")
    return tuple(i - j for i, j in zip(tuple_1, tuple_2))

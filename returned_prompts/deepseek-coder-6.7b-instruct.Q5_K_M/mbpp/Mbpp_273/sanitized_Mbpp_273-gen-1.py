def substract_elements(t1, t2):
    if len(t1) != len(t2):
        return 'Tuples must be of the same length'

    return tuple(x1 - x2 for (x1, x2) in zip(t1, t2))
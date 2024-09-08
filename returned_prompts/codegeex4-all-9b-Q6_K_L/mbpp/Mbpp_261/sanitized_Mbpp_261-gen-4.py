def division_elements(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Both tuples must have the same length")

    return tuple(a / b for a, b in zip(t1, t2))
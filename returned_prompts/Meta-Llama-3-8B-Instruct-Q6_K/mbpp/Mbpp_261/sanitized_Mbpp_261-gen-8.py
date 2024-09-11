def division_elements(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length")
    return tuple(i / j for i, j in zip(tuple1, tuple2))
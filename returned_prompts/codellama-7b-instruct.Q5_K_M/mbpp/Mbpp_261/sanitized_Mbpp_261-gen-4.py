def division_elements(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must be of same length")
    return tuple(int(i) // int(j) for i, j in zip(tuple1, tuple2))
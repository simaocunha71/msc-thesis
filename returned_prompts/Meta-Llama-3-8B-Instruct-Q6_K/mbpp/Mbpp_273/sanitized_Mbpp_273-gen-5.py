def substract_elements(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length")
    return tuple(t1[i] - t2[i] for i in range(len(t1)))  # or use map and subtract
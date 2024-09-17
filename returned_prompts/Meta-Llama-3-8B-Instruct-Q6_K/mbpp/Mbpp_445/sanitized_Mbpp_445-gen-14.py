def index_multiplication(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length")

    result = tuple(a * b for a, b in zip(t1, t2))
    return result
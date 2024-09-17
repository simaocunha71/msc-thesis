def average_tuple(tuples):
    if not isinstance(tuples, tuple):
        raise ValueError("Input must be a tuple of tuples")
    for t in tuples:
        if not isinstance(t, tuple):
            raise ValueError("Input must be a tuple of tuples")
        if len(t) == 0:
            raise ValueError("Tuple cannot have zero elements")
    return [sum(t)/len(t) for t in tuples]
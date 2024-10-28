def div_list(a, b):
    if len(a) != len(b):
        raise ValueError("Both lists must have the same length")
    return [float(x) / y for x, y in zip(a, b)]
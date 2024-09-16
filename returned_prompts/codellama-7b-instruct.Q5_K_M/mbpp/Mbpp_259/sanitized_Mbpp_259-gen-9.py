def maximize_elements(t1, t2):
    return tuple(
        tuple(max(x, y) for x, y in zip(t1_i, t2_i))
        for t1_i, t2_i in zip(t1, t2)
    )
def and_tuples(t1, t2):
    result = ()
    for a, b in zip(t1, t2):
        if a and b:
            result += (1,)
        else:
            result += (0,)
    return result
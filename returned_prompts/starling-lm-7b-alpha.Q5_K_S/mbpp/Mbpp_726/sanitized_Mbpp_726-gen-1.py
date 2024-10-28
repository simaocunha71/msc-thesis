def multiply_elements(t):
    if len(t) == 0:
        return ()
    return tuple(map(lambda x: x[0] * x[1], zip(t[:-1], t[1:])))
t = (1, 5, 7, 8, 10)
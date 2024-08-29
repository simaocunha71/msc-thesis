def tuple_modulo(t1, t2):
    return tuple(a % b for a, b in zip(t1, t2))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))

#output: (0, 4, 5, 1)



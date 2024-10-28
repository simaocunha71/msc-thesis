def tuple_modulo(tuple_a, tuple_b):
    result = []
    for i in range(len(tuple_a)):
        result.append(tuple_a[i] % tuple_b[i])
    return tuple(result)



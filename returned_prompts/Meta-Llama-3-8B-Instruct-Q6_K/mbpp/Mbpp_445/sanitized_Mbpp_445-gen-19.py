def index_multiplication(t1, t2):
    result = []
    for a, b in zip(t1, t2):
        result.append(tuple(x*y for x, y in zip(a, b)))
    return tuple(result)
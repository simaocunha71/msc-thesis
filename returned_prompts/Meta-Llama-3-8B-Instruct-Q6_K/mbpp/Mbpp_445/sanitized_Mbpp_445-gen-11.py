def index_multiplication(tuples):
    result = []
    for t1, t2 in zip(tuples[0], tuples[1]):
        result.append(tuple(i * j for i, j in zip(t1, t2)))
    return tuple(result)
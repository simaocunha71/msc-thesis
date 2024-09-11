def index_multiplication(tuple1, tuple2):
    result = []
    for t1, t2 in zip(tuple1, tuple2):
        result.append((t1[0]*t2[0], t1[1]*t2[1]))
    return tuple(result)
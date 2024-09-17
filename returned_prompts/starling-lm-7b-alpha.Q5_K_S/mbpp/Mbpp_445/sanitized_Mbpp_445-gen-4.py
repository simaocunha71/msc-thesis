def index_multiplication(t1, t2):
    # assert len(t1) == len(t2)
    result = []
    for i in range(len(t1)):
        result.append((t1[i] * t2[i]))
    return tuple(result)
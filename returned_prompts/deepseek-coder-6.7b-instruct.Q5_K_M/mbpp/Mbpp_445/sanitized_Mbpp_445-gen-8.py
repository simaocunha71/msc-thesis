def index_multiplication(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        if type(tup1[i]) == tuple and type(tup2[i]) == tuple:
            result.append(tuple(x * y for x, y in zip(tup1[i], tup2[i])))
        else:
            result.append(tup1[i] * tup2[i])
    return tuple(result)
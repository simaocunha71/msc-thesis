def index_multiplication(tup1, tup2):
    if len(tup1) != len(tup2):
        return None
    else:
        result = []
        for i in range(len(tup1)):
            result.append((tup1[i] * tup2[i]))
        return tuple(result)
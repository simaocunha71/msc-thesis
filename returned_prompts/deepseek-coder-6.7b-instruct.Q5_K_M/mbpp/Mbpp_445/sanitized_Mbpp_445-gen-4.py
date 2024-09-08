def index_multiplication(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        temp = []
        for j in range(len(tup1[i])):
            temp.append(tup1[i][j] * tup2[i][j])
        result.append(tuple(temp))
    return tuple(result)
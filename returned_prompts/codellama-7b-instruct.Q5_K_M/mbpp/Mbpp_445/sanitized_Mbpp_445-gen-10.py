def index_multiplication(tuple_1,tuple_2):
    result = []
    for i in range(len(tuple_1)):
        result.append((tuple_1[i][0] * tuple_2[i][0], tuple_1[i][1] * tuple_2[i][1]))
    return result
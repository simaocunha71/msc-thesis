def index_multiplication(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        result.append((tup1[i][0]*tup2[i][0], tup1[i][1]*tup2[i][1]))
    return tuple(result)  # Return the result as a tuple
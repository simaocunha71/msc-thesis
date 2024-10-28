def substract_elements(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i] - tup2[i])
    return tuple(result)
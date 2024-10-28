def division_elements(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        if tup2[i] != 0:
            result.append(tup1[i] / tup2[i])
        else:
            result.append(None)
    return tuple(result)
def and_tuples(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        if tup1[i] & tup2[i]:
            result.append(1)
        else:
            result.append(0)
    return tuple(result)


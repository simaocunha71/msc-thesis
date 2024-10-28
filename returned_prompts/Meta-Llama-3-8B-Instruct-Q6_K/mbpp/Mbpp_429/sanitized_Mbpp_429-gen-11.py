def and_tuples(t1, t2):
    result = []
    for i in range(len(t1)):
        if t1[i] == t2[i]:
            result.append(i)
    return tuple(result)
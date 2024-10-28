def and_tuples(t1, t2):
    result = []
    for i in range(min(len(t1), len(t2))):
        result.append(t1[i] & t2[i])
    return tuple(result)
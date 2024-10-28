def and_tuples(t1, t2):
    result = []
    for i, _ in enumerate(t1):
        if t1[i] and t2[i]:
            result.append(i)
    return result
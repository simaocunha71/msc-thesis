def maximize_elements(tuples1, tuples2):
    result = []
    for t1, t2 in zip(tuples1, tuples2):
        if t1[1] > t2[1]:
            result.append(t1)
        else:
            result.append(t2)
    return tuple(result)
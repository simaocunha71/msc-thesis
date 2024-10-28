def division_elements(t1, t2):
    if len(t1) != len(t2):
        raise ValueError('Both tuples should have the same length')
    result = []
    for i in range(len(t1)):
        if t2[i] != 0:
            result.append(t1[i] / t2[i])
        else:
            result.append(None)
    return tuple(result)
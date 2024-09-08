def maximize_elements(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append((max(t1[i][0], t2[i][0]), max(t1[i][1], t2[i][1])))
    return tuple(result)
def maximize_elements(t1, t2):
    res = []
    for i in range(len(t1)):
        if t1[i] > t2[i]:
            res.append(t1[i])
        else:
            res.append(t2[i])
    return tuple(res)
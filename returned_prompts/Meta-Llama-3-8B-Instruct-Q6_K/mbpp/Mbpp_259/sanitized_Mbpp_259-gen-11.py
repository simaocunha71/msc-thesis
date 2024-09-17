def maximize_elements(tuple1, tuple2):
    result = []
    for t1, t2 in zip(tuple1, tuple2):
        if t1[0] > t2[0]:
            result.append(t1)
        elif t2[0] > t1[0]:
            result.append(t2)
        else:
            if t1[1] > t2[1]:
                result.append(t1)
            else:
                result.append(t2)
    result.append(tuple2[-1])
    return tuple(result)
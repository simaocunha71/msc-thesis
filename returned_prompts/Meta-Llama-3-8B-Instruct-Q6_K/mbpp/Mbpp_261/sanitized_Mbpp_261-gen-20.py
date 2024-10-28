def division_elements(tuple1, tuple2):
    result = []
    for i in range(len(tuple1)):
        if tuple2[i] != 0:
            result.append(tuple1[i] / tuple2[i])
        else:
            result.append(None)
    return tuple(result)
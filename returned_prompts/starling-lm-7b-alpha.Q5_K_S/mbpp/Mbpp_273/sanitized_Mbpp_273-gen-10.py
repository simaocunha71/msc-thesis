def substract_elements(tuple1, tuple2):
    res = []
    for i in range(len(tuple1)):
        res.append(tuple1[i] - tuple2[i])
    return tuple(res)
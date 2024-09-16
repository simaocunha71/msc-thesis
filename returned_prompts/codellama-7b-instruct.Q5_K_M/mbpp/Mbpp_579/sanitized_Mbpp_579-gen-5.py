def find_dissimilar(tuple_1, tuple_2):
    result = []
    for i in tuple_1:
        if i not in tuple_2:
            result.append(i)
    for j in tuple_2:
        if j not in tuple_1:
            result.append(j)
    return tuple(result)
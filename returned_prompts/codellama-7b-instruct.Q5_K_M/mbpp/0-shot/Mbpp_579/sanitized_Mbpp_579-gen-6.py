def find_dissimilar(tuple1, tuple2):
    result = ()
    for i in tuple1:
        if i not in tuple2:
            result += (i,)
    for j in tuple2:
        if j not in tuple1:
            result += (j,)
    return result
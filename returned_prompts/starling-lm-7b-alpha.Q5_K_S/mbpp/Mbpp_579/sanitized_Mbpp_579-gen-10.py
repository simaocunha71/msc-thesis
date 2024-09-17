def find_dissimilar(tuple1, tuple2):
    diss_set = set(tuple1) & set(tuple2)
    return tuple(set(tuple1) - diss_set) + tuple(set(tuple2) - diss_set)
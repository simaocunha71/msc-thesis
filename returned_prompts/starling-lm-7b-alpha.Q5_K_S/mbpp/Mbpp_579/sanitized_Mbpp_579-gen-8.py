def find_dissimilar(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    result = tuple(set1.difference(set2))
    return result
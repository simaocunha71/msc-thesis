def find_dissimilar(tuple1, tuple2):
    for i in tuple1:
        if i not in tuple2:
            return i
    for i in tuple2:
        if i not in tuple1:
            return i
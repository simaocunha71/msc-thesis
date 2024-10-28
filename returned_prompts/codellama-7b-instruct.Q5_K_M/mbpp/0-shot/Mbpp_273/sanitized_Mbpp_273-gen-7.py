def substract_elements(tuple1, tuple2):
    return tuple(t1 - t2 for t1, t2 in zip(tuple1, tuple2))
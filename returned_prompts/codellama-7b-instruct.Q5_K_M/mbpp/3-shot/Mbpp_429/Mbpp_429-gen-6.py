
def and_tuples(test_tuple1, test_tuple2):
    return tuple(i & j for i, j in zip(test_tuple1, test_tuple2))



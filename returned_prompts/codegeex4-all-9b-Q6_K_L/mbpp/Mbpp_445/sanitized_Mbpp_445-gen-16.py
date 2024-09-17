def index_multiplication(test_tuple1, test_tuple2):
    if len(test_tuple1) != len(test_tuple2):
        return "Tuples must be of the same length"
    else:
        return tuple(map(lambda x: (x[0]*x[1]), zip(test_tuple1, test_tuple2)))
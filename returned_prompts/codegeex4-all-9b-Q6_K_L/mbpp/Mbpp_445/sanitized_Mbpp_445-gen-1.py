def index_multiplication(tuple1, tuple2):
    result = []
    for t1, t2 in zip(tuple1, tuple2):
        multiplied_elements = tuple(map(lambda x, y: x * y, t1, t2))
        result.append(multiplied_elements)
    return tuple(result)
def division_elements(tuple1, tuple2):
    if not tuple2:
        return tuple1
    result = tuple(i/j for i, j in zip(tuple1, tuple2))
    return result
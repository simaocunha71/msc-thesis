def union_elements(tuple1, tuple2):
    """
    Find the union of the elements of two given tuples and output them in sorted order.
    """
    tuple1 = set(tuple1)
    tuple2 = set(tuple2)
    union_set = tuple1.union(tuple2)
    union_tuple = tuple(sorted(union_set))
    return union_tuple
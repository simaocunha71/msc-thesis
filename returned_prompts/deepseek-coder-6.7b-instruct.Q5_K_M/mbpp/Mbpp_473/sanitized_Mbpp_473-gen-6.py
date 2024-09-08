def tuple_intersection(tuple_list):
    intersection = set(tuple_list[0])
    for tuples in tuple_list[1:]:
        intersection &= set(tuples)
    return intersection
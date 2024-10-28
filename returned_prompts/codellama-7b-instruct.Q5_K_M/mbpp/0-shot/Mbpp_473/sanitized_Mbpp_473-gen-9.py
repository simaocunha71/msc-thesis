def tuple_intersection(tuple_list):
    intersection = set()
    for t in tuple_list:
        intersection |= set(t)
    return tuple(intersection)
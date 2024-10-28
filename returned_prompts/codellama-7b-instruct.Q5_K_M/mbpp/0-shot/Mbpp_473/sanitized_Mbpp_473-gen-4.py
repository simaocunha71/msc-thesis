def tuple_intersection(tuple_list):
    if not tuple_list:
        return set()
    intersection = set(tuple_list[0])
    for t in tuple_list:
        intersection &= set(t)
    return intersection
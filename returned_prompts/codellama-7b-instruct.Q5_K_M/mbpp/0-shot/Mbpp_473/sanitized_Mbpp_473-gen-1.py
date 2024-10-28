def tuple_intersection(tuple_list):
    intersection = set()
    for t in tuple_list:
        for e in t:
            if e in intersection:
                continue
            intersection.add(e)
    return intersection
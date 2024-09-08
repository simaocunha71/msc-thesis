def tuple_intersection(tuples):
    result = set(tuples[0])
    for tup in tuples[1:]:
        result &= set(tup)
    return result
tuples = [(3, 4),  (5, 6),  (9, 10),  (4, 5)] , [(5, 4),  (3, 4),  (6, 5),  (9, 11)]
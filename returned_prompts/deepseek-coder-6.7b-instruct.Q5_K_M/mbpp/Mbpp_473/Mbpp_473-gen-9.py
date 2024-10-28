
def tuple_intersection(tuples1, tuples2):
    tuples1 = [tuple(sorted(list(t))) for t in tuples1]
    tuples2 = [tuple(sorted(list(t))) for t in tuples2]
    return set(tuples1) & set(tuples2)



def max_aggregate(tuples: list) -> tuple:
    max_val = 0
    max_tuple = ()
    for tup in tuples:
        if tup[1] > max_val:
            max_val = tup[1]
            max_tuple = tup
    return max_tuple


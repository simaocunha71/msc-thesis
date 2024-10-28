def max_aggregate(list_of_tuples):
    max_sum = 0
    max_tuple = None
    for tup in list_of_tuples:
        if tup[1] > max_sum:
            max_sum = tup[1]
            max_tuple = tup
    return max_tuple
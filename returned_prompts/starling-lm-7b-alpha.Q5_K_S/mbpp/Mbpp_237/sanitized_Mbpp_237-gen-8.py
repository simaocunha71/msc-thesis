def check_occurences(list_of_tuples):
    d = {}
    for tup in list_of_tuples:
        if tup in d:
            d[tup] += 1
        else:
            d[tup] = 1
    return d
list_of_tuples = [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]

def combinations_list(my_list):
    return [list(i) for i in itertools.combinations(my_list, len(my_list))]



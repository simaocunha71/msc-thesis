def consecutive_duplicates(my_list):
    return list(map(lambda x: x[0], itertools.groupby(my_list)))

def pack_consecutive_duplicates(my_list):
    return [list(g) for k,g in itertools.groupby(my_list)]



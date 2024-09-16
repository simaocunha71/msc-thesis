def pack_consecutive_duplicates(my_list):
    return [list(g) for k, g in groupby(my_list)]
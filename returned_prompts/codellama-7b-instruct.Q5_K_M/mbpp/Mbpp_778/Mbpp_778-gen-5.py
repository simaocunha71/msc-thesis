
def pack_consecutive_duplicates(my_list: list):
    return [list(g) for k, g in groupby(my_list)]



def get_equal(tup):
    len_list = [len(i) for i in tup]
    return len_list.count(len_list[0]) == len(len_list)
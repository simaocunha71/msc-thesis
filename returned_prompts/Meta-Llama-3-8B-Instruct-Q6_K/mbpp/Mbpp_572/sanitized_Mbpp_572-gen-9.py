def two_unique_nums(lst):
    return list(set([i for i in lst if lst.count(i) == 1]))
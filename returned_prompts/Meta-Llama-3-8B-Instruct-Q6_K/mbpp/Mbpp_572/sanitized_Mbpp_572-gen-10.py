def two_unique_nums(lst):
    unique_nums = set(lst)
    return [i for i in unique_nums if lst.count(i) == 1]
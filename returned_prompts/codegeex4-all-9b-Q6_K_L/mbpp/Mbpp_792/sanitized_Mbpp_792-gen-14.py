def count_list(lst):
    return sum(1 for i in lst if isinstance(i, list))
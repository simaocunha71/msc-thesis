def consecutive_duplicates(lst):
    return [i for i in lst if lst.count(i) == 1]
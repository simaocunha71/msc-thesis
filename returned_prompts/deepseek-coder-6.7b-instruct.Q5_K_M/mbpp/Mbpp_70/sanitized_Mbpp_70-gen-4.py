def get_equal(lst):
    return all(len(x) == len(lst[0]) for x in lst)
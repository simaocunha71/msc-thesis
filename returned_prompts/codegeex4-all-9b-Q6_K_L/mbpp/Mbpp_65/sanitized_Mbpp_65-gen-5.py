def recursive_list_sum(lst):
    if not isinstance(lst, list):
        return lst
    return sum(recursive_list_sum(x) for x in lst)
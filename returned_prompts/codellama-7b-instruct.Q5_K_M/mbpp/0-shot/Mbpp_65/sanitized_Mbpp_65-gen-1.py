def recursive_list_sum(lst):
    if isinstance(lst, list):
        return sum(map(recursive_list_sum, lst))
    else:
        return lst
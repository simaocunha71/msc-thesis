def recursive_list_sum(lst):
    res = 0
    for item in lst:
        if isinstance(item, list):
            res += recursive_list_sum(item)
        else:
            res += item
    return res
def recursive_list_sum(lst):
    if not isinstance(lst, list):
        return lst
    total = 0
    for item in lst:
        total += recursive_list_sum(item)
    return total
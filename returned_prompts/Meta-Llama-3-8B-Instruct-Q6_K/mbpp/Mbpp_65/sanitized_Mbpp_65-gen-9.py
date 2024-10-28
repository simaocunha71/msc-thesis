def recursive_list_sum(lst):
    total = sum(i for i in lst if isinstance(i, int))
    for i in lst:
        if isinstance(i, list):
            total += recursive_list_sum(i)
    return total
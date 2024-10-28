def recursive_list_sum(lst):
    total_sum = sum(i for i in lst if isinstance(i, int))
    for i in lst:
        if isinstance(i, list):
            total_sum += recursive_list_sum(i)
    return total_sum
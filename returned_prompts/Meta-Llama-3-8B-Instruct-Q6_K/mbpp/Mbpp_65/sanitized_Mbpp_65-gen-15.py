def recursive_list_sum(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return lst[0][0] + recursive_list_sum(lst[0][1:]) + recursive_list_sum(lst[1:])
    else:
        return lst[0] + recursive_list_sum(lst[1:])
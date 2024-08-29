def recursive_list_sum(lst):
    if lst == []:
        return 0
    elif type(lst[0]) == list:
        return recursive_list_sum(lst[0]) + recursive_list_sum(lst[1:])
    else:
        return lst[0] + recursive_list_sum(lst[1:])
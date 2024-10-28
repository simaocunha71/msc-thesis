def recursive_list_sum(lst):
    total_sum = 0
    for i in lst:
        if type(i) == list:
            total_sum += recursive_list_sum(i)
        else:
            total_sum += i
    return total_sum
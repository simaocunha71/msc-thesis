def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total
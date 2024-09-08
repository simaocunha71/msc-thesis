def max_sum_list(lst):
    max_sum = 0
    max_list = []
    for sublist in lst:
        sublist_sum = sum(sublist)
        if sublist_sum > max_sum:
            max_sum = sublist_sum
            max_list = sublist
    return max_list
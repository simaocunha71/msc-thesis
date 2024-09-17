def max_sum_list(lst):
    max_sum = -float('inf')
    max_list = []
    for sublist in lst:
        if sum(sublist) > max_sum:
            max_sum = sum(sublist)
            max_list = sublist
    return max_list


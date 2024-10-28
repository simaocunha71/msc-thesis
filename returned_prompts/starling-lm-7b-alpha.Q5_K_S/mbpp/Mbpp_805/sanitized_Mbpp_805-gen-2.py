def max_sum_list(lst):
    max_sum = 0
    max_list = []
    for sublist in lst:
        cur_sum = sum(sublist)
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_list = sublist
    return max_list
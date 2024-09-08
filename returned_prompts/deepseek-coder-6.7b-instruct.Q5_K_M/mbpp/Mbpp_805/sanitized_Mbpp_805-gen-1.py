def max_sum_list(lst):
    max_sum = -float('inf')
    max_list = []
    for sub_lst in lst:
        if sum(sub_lst) > max_sum:
            max_sum = sum(sub_lst)
            max_list = sub_lst
    return max_list
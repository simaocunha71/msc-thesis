def max_sum_list(lst):
    max_sum = max(sum(sub_list) for sub_list in lst)
    return [sub_list for sub_list in lst if sum(sub_list) == max_sum][0]
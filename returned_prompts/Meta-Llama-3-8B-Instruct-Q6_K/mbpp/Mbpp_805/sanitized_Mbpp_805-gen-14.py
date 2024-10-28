def max_sum_list(list_of_lists):
    max_sum = float('-inf')
    max_sum_list = []
    for lst in list_of_lists:
        if sum(lst) > max_sum:
            max_sum = sum(lst)
            max_sum_list = lst
    return max_sum_list
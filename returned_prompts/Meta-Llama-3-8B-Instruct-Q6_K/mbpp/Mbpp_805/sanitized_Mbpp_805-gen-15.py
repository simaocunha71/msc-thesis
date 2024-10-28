def max_sum_list(lists):
    max_sum = 0
    max_list = []
    for lst in lists:
        if sum(lst) > max_sum:
            max_sum = sum(lst)
            max_list = lst
    return max_list
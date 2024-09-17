def max_sum_list(lst: list):
    max_sum = 0
    max_sum_list = []
    for sub_lst in lst:
        current_sum = sum(sub_lst)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_list = sub_lst
    return max_sum_list


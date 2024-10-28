def max_sum_list(lists):
    max_sum = float('-inf')
    max_list = []
    for lst in lists:
        total = sum(lst)
        if total > max_sum:
            max_sum = total
            max_list = lst
    return max_list
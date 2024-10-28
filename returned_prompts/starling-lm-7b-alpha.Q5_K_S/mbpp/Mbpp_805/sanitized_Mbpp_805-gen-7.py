def max_sum_list(lst):
    max_list = []
    for i in range(len(lst)):
        if sum(lst[i]) >= sum(max_list):
            max_list = lst[i]
    return max_list
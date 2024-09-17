def max_sum_list(test_list):
    max_sum = 0
    max_sum_list = []
    for sublist in test_list:
        if sum(sublist) > max_sum:
            max_sum = sum(sublist)
            max_sum_list = sublist
    return max_sum_list
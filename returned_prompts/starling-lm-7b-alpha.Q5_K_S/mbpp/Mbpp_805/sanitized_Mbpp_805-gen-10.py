def max_sum_list(lists):
    max_sum = 0
    max_list = []
    for l in lists:
        sum_ = sum(l)
        if sum_ > max_sum:
            max_sum = sum_
            max_list = l
    return max_list
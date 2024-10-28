def max_sum_list(l):
    max_sum = 0
    max_list = []
    for sublist in l:
        if sum(sublist) > max_sum:
            max_sum = sum(sublist)
            max_list = sublist
    return max_list
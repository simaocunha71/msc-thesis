def max_sum_list(lst):
    sums = [sum(sublist) for sublist in lst]
    max_sum_index = sums.index(max(sums))
    return lst[max_sum_index]


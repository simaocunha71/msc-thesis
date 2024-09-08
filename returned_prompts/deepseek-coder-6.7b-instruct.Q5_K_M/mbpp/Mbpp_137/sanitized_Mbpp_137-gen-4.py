def zero_count(lst):
    zero_num = lst.count(0)
    non_zero_num = len(lst) - zero_num
    return zero_num / non_zero_num
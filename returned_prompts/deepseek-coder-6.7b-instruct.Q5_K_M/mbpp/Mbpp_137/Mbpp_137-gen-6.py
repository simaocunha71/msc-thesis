
def zero_count(lst):
    zero = sum(i == 0 for i in lst)
    non_zero = sum(i != 0 for i in lst)
    return zero / non_zero if non_zero else float('inf')



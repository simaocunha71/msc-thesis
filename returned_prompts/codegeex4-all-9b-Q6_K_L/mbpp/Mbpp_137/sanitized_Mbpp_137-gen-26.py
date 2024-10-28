def zero_count(lst):
    num_of_zeroes = lst.count(0)
    num_of_non_zeroes = len(lst) - num_of_zeroes
    ratio = num_of_zeroes / num_of_non_zeroes
    return ratio
def sum_negativenum(lst):
    return sum(i for i in lst if i < 0)  # or sum(-x for x in lst if x < 0) to get the sum of negative numbers only
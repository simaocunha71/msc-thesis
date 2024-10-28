def sum_negativenum(lst):
    return sum(x for x in lst if x < 0)  # or sum(-i for i in lst if i < 0) for the same result
def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)  # or return sum(-x for x in lst if x < 0) for negative numbers only
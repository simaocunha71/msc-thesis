def sum_negativenum(lst):
    return sum([i for i in lst if i < 0])  # or return sum(-x for x in lst if x < 0) for a more concise solution.
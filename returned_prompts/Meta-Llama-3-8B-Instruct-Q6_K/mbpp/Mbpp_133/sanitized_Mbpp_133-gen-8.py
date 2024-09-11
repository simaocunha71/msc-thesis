def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)  # or return sum([i for i in lst if i < 0]) for a list comprehension
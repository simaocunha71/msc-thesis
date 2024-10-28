from functools import reduce
def recursive_list_sum(lst):
    # using reduce to sum all elements in the flattened list
    return reduce(lambda x, y: x + y, [i for sublist in lst for i in sublist])
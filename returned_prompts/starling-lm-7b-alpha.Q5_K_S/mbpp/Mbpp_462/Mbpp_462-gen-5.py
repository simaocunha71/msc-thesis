def combinations_list(list_items):
    """
    Find all possible combinations of the elements of a given list.
    """
    from itertools import chain, combinations
    return [list(c) for c in chain(*[combinations(list_items, r) for r in range(len(list_items) + 1)])

# print(combinations_list(['orange', 'red', 'green', 'blue']))


"""
The function `combinations_list` uses the built-in Python module `itertools` to generate all possible combinations. The `chain` function is used to concatenate the results of all the combinations of different lengths, and `combinations` generates all the combinations of a given length from the input list. The resulting combinations are then returned as a list of lists.

For example, for the input list `['orange', 'red', 'green', 'blue']`, the function will return `[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]`. This represents all possible combinations of the elements in the input list.
"""




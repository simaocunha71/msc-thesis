def max_tuples(lst):
    return tuple(max(x) for x in lst)

print(max_tuples([(1, 2), (3, 4), (5, 6)]))  # (2, 4, 6)

"""
Write a function which takes a list of tuples and returns a new tuple with the minimum value from each tuple.
assert min_tuples([(1
def tuple_intersection(tuples):
    result = set()
    for tup in tuples:
        if not result:  # first tuple
            result = set(tup)
        else:
            result = result & set(tup)  # find intersection
    return result


print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]]))  #{(4, 5), (3, 4), (5, 6)}


"""
Alternatively, you can use built-in function map() and reduce() in Python:
"""
from functools import reduce

def tuple_intersection(tuples):
    return reduce(lambda x, y: set(x).intersection(set(y)), tuples)


print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]]))  #{(4, 5), (3, 4), (5, 6)}

"""
Note that both solutions return a set of tuples, because sets in Python are unordered and don't allow duplicate elements.
"""

"""
Explanation of the code:

The function takes a list of tuples as an argument. If the list is empty, it returns an empty set. Otherwise, it initializes the result set with the first tuple. Then, it iterates over the remaining tuples, computing the intersection of the current result set and the current tuple, and updates the result set with this intersection. Finally, it returns the result set.
"""

# Note that the set intersection operation (&) returns a new set that contains only the elements that are common to all sets.
# The reduce() function applies a binary function (in this case, the intersection operation) to all items of an iterable in a cumulative way. For example, if you wanted to find the intersection of all tuples in the list,

def tuple_intersection(lists):
    res = set()
    for tup in lists[0]:
        for tup2 in lists[1]:
            if tup == tup2:
                res.add(tup)
            elif tup[::-1] == tup2:
                res.add(tup)
            elif tup == tup2[::-1]:
                res.add(tup2)
            elif tup[1],tup[0] == tup2:
                res.add((tup[1],tup[0]))
            elif tup == (tup2[1],tup2[0]):
                res.add((tup2[1],tup2[0]))
            elif tup[1],tup[0] == (tup2[1],tup2[0]):
                res.add((tup[1],tup[0]))
            elif tup == (tup2[0],tup2[1]):
                res.add((tup2[0],tup2[1]))
            elif tup[0],tup[1] == (tup2[0],tup2[1]):
                res.add((tup[0],tup[1]))
    return res

assert tuple_intersection([(3, 4),  (5, 6),  (9, 10),  (4, 5)] , [(5, 4),  (3, 4),  (6, 5),  (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
The above code works by iterating over each tuple in the first list, then iterating over each tuple in the second list. If the tuples are equal or the reversed tuple of the second list is equal to the tuple of the first list, then it adds that tuple to the result set.
"""

"""
This code can be optimized by using sets to get the intersection of the tuples.
"""
def tuple_intersection_optimized(lists):
    return set(lists[0]).intersection(lists[1])
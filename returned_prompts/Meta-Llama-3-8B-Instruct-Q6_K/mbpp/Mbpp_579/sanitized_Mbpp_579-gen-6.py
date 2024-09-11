def find_dissimilar(tup1, tup2):
    set1 = set(tup1)
    set2 = set(tup2)
    return tuple(sorted(list(set1.symmetric_difference(set2))))
    # return tuple(sorted(set1 ^ set2)) # alternative way using set operations
    # return tuple(sorted([x for x in tup1+tup2 if tup1.count(x) != tup2.count(x)])) # alternative way using list comprehension and count function
    # return tuple(sorted([x for x in tup1 if x not in tup2] + [x for x in tup2 if x not in tup1])) # alternative way using list comprehension and not in operator
    # return tuple(sorted([x for x in tup1 + tup2 if tup1.count(x) != tup2.count(x) or (x not in tup1 and x not in tup2)])) # alternative way using list comprehension, count function, and not in operator
    # return tuple(sorted([x for x in tup1 if x not in tup2] + [x for x in tup2 if x not in tup1])) # alternative way using list comprehension and not in operator
    # return tuple(sorted(list(set(tup1).symmetric_difference(set(tup2))))) # alternative way using set operations
    # return tuple(sorted(list(set(tup1).difference(set(tup2))) + list(set(tup2).difference(set(tup1))))) # alternative way using set operations
    # return tuple(sorted([x for x in tup1 if x not in tup2] + [x for x in tup2 if x not in tup1])) # alternative way using list comprehension and not in operator
    # return tuple(sorted([x for x in tup1 if x not in tup2] + [x for x in tup2 if x not in tup1])) # alternative way using list comprehension and not in operator
    # return tuple(sorted(list(set(tup1).union(set(tup2)).difference(tup1.union(tup2))))) # alternative way using set operations
    # return tuple(sorted(list(set(tup1).union(set(tup2)).difference(set(tup1).union(set(tup2)))))) # alternative way using set operations
    # return tuple(sorted(list(set(tup1).union(set(tup2)).difference(set(tup1).union(set(tup2)))))) # alternative way using set operations
    # return tuple
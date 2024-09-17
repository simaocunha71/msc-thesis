def unique_sublists(lst):
    tuples = set()
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in tuples:
            tuples.add(tuple_sublist)
    return {k: lst.count(k) for k in tuples}
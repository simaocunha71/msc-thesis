def unique_sublists(lst):
    sublists = {}
    for i in range(len(lst)):
        sub = lst[i]
        tuple_sub = tuple(sorted(sub))
        if tuple_sub not in sublists:
            sublists[tuple_sub] = 1
        else:
            sublists[tuple_sub] += 1
    return sublists

def unique_sublists(lst):
    sublists = {}
    for sub in lst:
        sub = tuple(sorted(sub))
        if sub not in sublists:
            sublists[sub] = 1
        else:
            sublists[sub] += 1
    return sublists





















"""
def unique_sublists(lst):
    sublists = {}
    for i in range(len(lst)):
        sub = lst[i]
        tuple_sub = tuple(sorted(sub))
        if tuple_sub not in sublists:
            sublists[tuple_sub] = 1
        else:
            sublists[tuple_sub] += 1
    return sublists

def unique_sublists(lst):
    sublists = {}
    for sub in lst:
        sub = tuple(sorted(sub))
        if sub not in sublists:
            sublists[sub] = 1
        else:
            sublists[sub] += 1
    return sublists
"""



















































































"""
def unique_sublists(lst):
    sublists = {}
    for sub in lst:
        sub = tuple(sorted(sub))
        if sub not in sublists:
            sublists[sub] = 1
        else:
            sublists[sub] += 1
    return sublists

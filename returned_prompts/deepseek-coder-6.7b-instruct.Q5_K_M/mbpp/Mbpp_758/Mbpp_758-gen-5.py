
def unique_sublists(lst):
    return {tuple(l): lst.count(l) for l in lst}

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

Output:

{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

def unique_sublists(lst):
    count_dict = {}
    for l in lst:
        tuple_l = tuple(l)
        if tuple_l in count_dict:
            count_dict[tuple_l] += 1
        else:
            count_dict[tuple_l] = 1
    return count_dict

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

Output:

{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
"""

def unique_sublists(lst):
    count_dict = {}
    for l in lst:
        tuple_l = tuple(l)
        count_dict[tuple_l] = count_dict.get(tuple_l, 0) + 1
    return count_dict

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

Output:

{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
"""

def unique_sublists(lst):
"""
def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    else:
        return [[lst[0]] + sub_combs for sub_combs in combinations_list(lst[1:])]
"""

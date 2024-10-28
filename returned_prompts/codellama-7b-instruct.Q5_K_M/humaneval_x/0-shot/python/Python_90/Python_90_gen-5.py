
def next_smallest(lst):
    if len(lst) == 0: return None
    lst.sort()
    return lst[1]

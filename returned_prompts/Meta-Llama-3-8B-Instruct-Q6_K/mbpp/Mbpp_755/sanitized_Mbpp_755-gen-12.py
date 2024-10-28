def second_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    lst.sort()
    return lst[1]
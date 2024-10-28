def consecutive_duplicates(lst):
    return [x for i, x in enumerate(lst) if i == 0 or x != lst[i-1]]
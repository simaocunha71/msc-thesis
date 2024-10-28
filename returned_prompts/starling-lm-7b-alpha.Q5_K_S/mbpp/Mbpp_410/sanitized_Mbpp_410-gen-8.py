def min_val(lst):
    minimum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
    return minimum
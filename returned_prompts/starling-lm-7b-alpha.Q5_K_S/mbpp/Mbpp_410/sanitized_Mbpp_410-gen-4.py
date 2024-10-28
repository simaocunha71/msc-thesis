def min_val(lst):
    min_val = lst[0]
    for i in range(1, len(lst)):
        if min_val > lst[i]:
            min_val = lst[i]
    return min_val
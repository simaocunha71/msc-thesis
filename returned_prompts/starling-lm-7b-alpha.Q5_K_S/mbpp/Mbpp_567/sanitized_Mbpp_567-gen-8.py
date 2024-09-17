def issort_list(lst):
    result = False
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            result = True
            break
    return result
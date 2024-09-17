def comb_sort(lst):
    gap = len(lst)
    shrink = 1.3
    sorted = False

    while gap > 1 or not sorted:
        gap = max(1, int(gap / shrink))
        sorted = True
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                sorted = False
    return lst
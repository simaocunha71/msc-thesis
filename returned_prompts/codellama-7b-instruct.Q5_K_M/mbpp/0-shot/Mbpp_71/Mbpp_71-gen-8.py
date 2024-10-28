def comb_sort(lst):
    gap = len(lst)
    swapped = True
    while gap > 1 or swapped:
        if gap > 1:
            gap = int(gap / 1.247330950103979)
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

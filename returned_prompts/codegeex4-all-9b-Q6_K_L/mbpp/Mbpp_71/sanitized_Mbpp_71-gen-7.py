def comb_sort(lst):
    gap = len(lst)
    while gap > 1:
        gap = (gap * 10) // 13
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
    return lst
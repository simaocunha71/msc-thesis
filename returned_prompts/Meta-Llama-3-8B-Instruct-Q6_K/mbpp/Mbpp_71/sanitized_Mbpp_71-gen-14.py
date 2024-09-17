def comb_sort(lst):
    swap = True
    gap = len(lst)
    while gap > 1 or swap:
        gap = max(1, int(gap / 1.3))
        swap = False
        i = 0
        while i + gap < len(lst):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swap = True
            i += 1
    return lst
def comb_sort(lst):
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            j = i
            while j >= gap and lst[j - gap] > lst[j]:
                lst[j - gap], lst[j] = lst[j], lst[j - gap]
                j -= gap
        gap //= 2
    return lst
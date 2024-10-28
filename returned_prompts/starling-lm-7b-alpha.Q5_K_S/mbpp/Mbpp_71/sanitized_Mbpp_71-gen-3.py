def comb_sort(lst):
    n = len(lst)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = gap / 1.3
        swapped = False
        for i in range(n - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst
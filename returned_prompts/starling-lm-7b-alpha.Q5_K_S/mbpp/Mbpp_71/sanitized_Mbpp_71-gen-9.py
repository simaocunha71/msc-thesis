def comb_sort(lst):
    n = len(lst)
    gap = n + 1
    swapped = True
    while gap != 1 or swapped:
        gap = gap//2
        swapped = False
        for i in range(n-gap):
            if lst[i] > lst[i+gap]:
                lst[i], lst[i+gap] = lst[i+gap], lst[i]
                swapped = True
    return lst
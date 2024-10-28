def comb_sort(lst):
    def swap(i, j):
        lst[i], lst[j] = lst[j], lst[i]

    gap = len(lst)
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False

        for i in range(len(lst) - gap):
            j = i + gap
            if lst[i] > lst[j]:
                swap(i, j)
                swapped = True

    return lst
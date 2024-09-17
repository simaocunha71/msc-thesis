
def comb_sort(lst):
    gap = len(lst)
    shrink = 1.3
    sorted = False

    while gap > 1 or not sorted:
        gap = max(1, int(gap / shrink))
        sorted = True

        for i in range(len(lst) - gap):
            j = i + gap
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                sorted = False

    return lst



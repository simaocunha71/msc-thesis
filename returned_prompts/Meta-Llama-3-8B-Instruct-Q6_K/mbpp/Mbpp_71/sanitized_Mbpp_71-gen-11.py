def comb_sort(lst):
    if len(lst) <= 1:
        return lst
    gap = len(lst)
    shrink = 1.3
    sorted_lst = lst[:]
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap > 1:
            swapped = False
            for i in range(len(lst) - gap):
                j = i + gap
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                    swapped = True
        else:
            gap = 1
            if not swapped:
                break
    return sorted_lst
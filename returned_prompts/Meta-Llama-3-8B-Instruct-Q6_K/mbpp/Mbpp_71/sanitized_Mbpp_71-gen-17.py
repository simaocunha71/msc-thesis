def comb_sort(lst):
    def gap_insertion_sort(lst, gap):
        for i in range(gap, len(lst)):
            key = lst[i]
            j = i
            while j >= gap and key < lst[j]:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = key

    gap = len(lst)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        for i in range(gap, len(lst)):
            if lst[i - gap] > lst[i]:
                gap_insertion_sort(lst, gap)
                sorted = False
                break

    return lst
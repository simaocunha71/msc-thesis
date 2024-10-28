def comb_sort(lst):
    def swap(i, j):
        lst[i], lst[j] = lst[j], lst[i]

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

        i = 0
        while i + gap < len(lst):
            if lst[i] > lst[i + gap]:
                swap(i, i + gap)
                sorted = False
            i += 1

    return lst
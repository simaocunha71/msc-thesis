import random
def comb_sort(lst):
    def swap(i, j):
        lst[i], lst[j] = lst[j], lst[i]

    gap = len(lst)
    shrink = 1.3

    while gap > 1:
        for i in range(0, len(lst) - gap):
            if lst[i] > lst[i + gap]:
                swap(i, i + gap)
        gap /= shrink
    return lst
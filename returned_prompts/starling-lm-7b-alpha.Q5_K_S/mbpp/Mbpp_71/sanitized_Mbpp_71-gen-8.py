def comb_sort(list_):
    n = len(list_)
    gap = n + 1
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        swapped = False

        for i in range(n - gap):
            if list_[i] > list_[i + gap]:
                list_[i], list_[i + gap] = list_[i + gap], list_[i]
                swapped = True

    return list_
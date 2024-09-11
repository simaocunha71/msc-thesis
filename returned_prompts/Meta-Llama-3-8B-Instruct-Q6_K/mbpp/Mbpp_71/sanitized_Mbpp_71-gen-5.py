def comb_sort(lst):
    def insertion_sort(start, end):
        for i in range(start + 1, end + 1):
            key = lst[i]
            j = i - 1
            while j >= start and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key

    gap = len(lst)
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False

        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True

        if not swapped:
            break

        insertion_sort(0, len(lst) - gap - 1)

    return lst
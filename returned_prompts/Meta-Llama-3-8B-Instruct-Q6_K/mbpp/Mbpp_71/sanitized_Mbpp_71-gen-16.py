def comb_sort(lst):
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    gap = len(lst)
    shrink = 1.3

    lst = lst[:]
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
        if swapped:
            gap = int(gap)
        else:
            break

    return insertion_sort(lst)
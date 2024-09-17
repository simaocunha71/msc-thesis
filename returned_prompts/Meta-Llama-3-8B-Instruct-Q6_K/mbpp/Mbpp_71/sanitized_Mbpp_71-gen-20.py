def comb_sort(arr):
    if not arr:
        return []

    gap = len(arr)
    shrink = 1.3

    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)

        if gap < 1:
            gap = 1

        swapped = False

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr
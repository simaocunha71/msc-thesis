def shell_sort(arr):
    # Start with a big gap, then reduce the gap
    gap = len(arr) // 2
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        for i in range(gap, len(arr)):
            # add a[i] to the elements that have been gap sorted
            temp = arr[i]
            # shift earlier gap-sorted elements up until the correct location
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        # reduce the gap
        gap //= 2
    return arr
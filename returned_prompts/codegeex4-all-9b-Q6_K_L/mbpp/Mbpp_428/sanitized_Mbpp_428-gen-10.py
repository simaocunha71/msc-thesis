def shell_sort(arr):
    def insertion_sort(arr, start, gap):
        for i in range(start + gap, len(arr), gap):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key

    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            insertion_sort(arr, i, gap)
        gap //= 2
    return arr
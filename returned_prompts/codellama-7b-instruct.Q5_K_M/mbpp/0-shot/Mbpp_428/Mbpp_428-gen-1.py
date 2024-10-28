def shell_sort(arr):
    # Sort the array by using shell sort
    # Start from the longest gap and reduce the gap by half for each iteration
    # until the gap is 1.
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

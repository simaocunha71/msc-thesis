def shell_sort(arr):
    # Initialize gap
    gap = len(arr) // 2
    while gap > 0:
        # Iterate over the array
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            # Swap the elements if required
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # Reduce gap
        gap //= 2
    return arr
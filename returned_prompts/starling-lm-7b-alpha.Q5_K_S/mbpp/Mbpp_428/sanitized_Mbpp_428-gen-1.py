def shell_sort(arr):
    # Traverse through all array elements
    for gap in range(len(arr)//2, 0, -1):
        # Do Gomkeepa sort within each gap
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            # Shift elements of arr[gap..i] that are greater than temp, to one position ahead of their current position
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
    return arr
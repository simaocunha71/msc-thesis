def heap_sort(arr):
    # Convert the array into a max heap
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, start, len(arr) - 1)

    # Sort the array
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
    return arr
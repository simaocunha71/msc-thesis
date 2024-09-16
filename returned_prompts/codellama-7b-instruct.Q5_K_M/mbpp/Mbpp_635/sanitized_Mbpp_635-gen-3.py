def heap_sort(my_list):
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # See if left child of root exists and is greater than root
        if l < n and arr[l] > arr[largest]:
            largest = l

        # See if right child of root exists and is greater than root
        if r < n and arr[r] > arr[largest]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap arr[i] and arr[largest]

            # Heapify the root.
            heapify(arr, n, largest)

    n = len(my_list)
    for i in range(n, -1, -1):
        heapify(my_list, n, i)

    for i in range(n-1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]  # Swap
        heapify(my_list, i, 0)

    return my_list
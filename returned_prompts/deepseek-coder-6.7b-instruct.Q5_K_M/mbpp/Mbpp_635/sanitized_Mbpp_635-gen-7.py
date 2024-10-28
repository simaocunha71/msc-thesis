def heap_sort(lst):
    n = len(lst)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(lst, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]   # swap
        heapify(lst, i, 0)
    return lst
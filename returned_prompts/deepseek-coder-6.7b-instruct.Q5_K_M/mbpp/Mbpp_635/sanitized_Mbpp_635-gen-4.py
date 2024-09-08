def heap_sort(lst):
    # Convert list into heap
    for i in range(len(lst)):
        heapify(lst, len(lst), i)
    # One by one extract elements
    for i in range(len(lst)-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i] # swap
        heapify(lst, i, 0)
    return lst
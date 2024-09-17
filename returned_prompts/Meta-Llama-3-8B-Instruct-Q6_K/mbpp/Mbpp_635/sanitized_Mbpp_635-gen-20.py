def heap_sort(lst):
    for i in range(len(lst)//2-1, -1, -1):
        heapify(lst, i, len(lst))
    for i in range(len(lst)-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i)
    return lst
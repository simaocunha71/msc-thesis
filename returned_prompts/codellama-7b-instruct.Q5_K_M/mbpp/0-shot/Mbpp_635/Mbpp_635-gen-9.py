def heap_sort(my_list):
    def heapify(my_list, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and my_list[i] < my_list[l]:
            largest = l
        if r < n and my_list[largest] < my_list[r]:
            largest = r
        if largest != i:
            my_list[i], my_list[largest] = my_list[largest], my_list[i]
            heapify(my_list, n, largest)

    n = len(my_list)
    for i in range(n, -1, -1):
        heapify(my_list, n, i)
    for i in range(n - 1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        heapify(my_list, i, 0)
    return my_list

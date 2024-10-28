def heap_sort(my_list):
    build_max_heap(my_list)
    for i in range(len(my_list)-1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        heapify(my_list, i, 0)
    return my_list
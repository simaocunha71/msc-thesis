def heap_sort(my_list):
    heapq.heapify(my_list)
    for i in range(len(my_list)-1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        heapq.heapify(my_list[:i])
    return my_list
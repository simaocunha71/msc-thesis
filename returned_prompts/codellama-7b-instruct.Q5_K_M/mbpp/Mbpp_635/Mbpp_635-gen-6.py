
from heapq import heapify, heappop, heappush

def heap_sort(my_list):
    heapify(my_list)
    for i in range(len(my_list)-1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        heappop(my_list)
    return my_list

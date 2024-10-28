def heap_sort(my_list):
    build_max_heap(my_list)
    for i in range(len(my_list)-1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        heapify(my_list, i, 0)
    return my_list

def build_max_heap(my_list):
    for i in range(len(my_list)//2, -1, -1):
        heapify(my_list, len(my_list), i)

def heapify(my_list, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and my_list[largest] < my_list[l]:
        largest = l
    if r < n and my_list[largest] < my_list[r]:
        largest = r
    if largest != i:
        my_list[i], my_list[largest] = my_list[largest], my_list[i]
        heapify(my_list, n, largest)

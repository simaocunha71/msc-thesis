
def heap_sort(my_list):
    build_max_heap(my_list)
    for i in range(len(my_list)-1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        heapify(my_list, i, 0)
    return my_list


def build_max_heap(my_list):
    for i in range(len(my_list)//2, -1, -1):
        heapify(my_list, len(my_list), i)


def heapify(my_list, size, i):
    largest = i
    left = (2*i)+1
    right = (2*i)+2
    if left < size and my_list[left] > my_list[largest]:
        largest = left
    if right < size and my_list[right] > my_list[largest]:
        largest = right
    if largest != i:
        my_list[largest], my_list[i] = my_list[i], my_list[largest]
        heapify(my_list, size, largest)

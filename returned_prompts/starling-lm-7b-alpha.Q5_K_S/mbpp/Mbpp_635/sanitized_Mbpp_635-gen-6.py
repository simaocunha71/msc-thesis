def heap_sort(lst):
    def max_heapify(lst, i, heap_size):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < heap_size and lst[left] > lst[largest]:
            largest = left
        if right < heap_size and lst[right] > lst[largest]:
            largest = right
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            max_heapify(lst, largest, heap_size)

    def heap_sort_recursive(lst, heap_size, end):
        if end:
            max_heapify(lst, 0, end)
            lst[0], lst[end - 1] = lst[end - 1], lst[0]
            heap_size -= 1
            heap_sort_recursive(lst, heap_size, end - 1)

    heap_size = len(lst)
    heap_sort_recursive(lst, heap_size, 1)
    return lst
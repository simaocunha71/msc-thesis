def heap_sort(lst):
    heap = list(lst)
    for i in range(len(heap) // 2 - 1, -1, -1):
        heapify(heap, i, len(heap))
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, 0, i)
    return heap
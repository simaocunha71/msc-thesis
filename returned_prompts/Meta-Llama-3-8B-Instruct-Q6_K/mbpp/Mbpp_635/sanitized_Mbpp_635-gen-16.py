def heap_sort(lst):
    if len(lst) > 0:
        heap = lst[:]
        heapify(heap, len(heap))
        sorted_list = []
        while len(heap) > 0:
            sorted_list.append(heap[0])
            heap[0] = heap[-1]
            heap.pop()
            heapify(heap, len(heap))
        return sorted_list[::-1]
    return []
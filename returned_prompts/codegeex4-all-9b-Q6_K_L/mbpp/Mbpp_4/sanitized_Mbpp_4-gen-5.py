def heap_queue_largest(numbers, n):
    import heapq
    heap = heapq.nlargest(n, numbers)
    return heap
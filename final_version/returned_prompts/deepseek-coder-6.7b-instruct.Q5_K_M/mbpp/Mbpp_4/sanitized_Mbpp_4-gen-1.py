def heap_queue_largest(numbers, k):
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)
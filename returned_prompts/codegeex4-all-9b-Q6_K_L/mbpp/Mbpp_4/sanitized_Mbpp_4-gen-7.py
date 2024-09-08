def heap_queue_largest(nums, n):
    import heapq
    heap = []
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)
    return sorted(heap, reverse=True)
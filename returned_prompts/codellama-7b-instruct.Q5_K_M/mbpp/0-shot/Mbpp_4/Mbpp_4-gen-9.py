"""
def heap_queue_largest(nums, n):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, -num)
        if len(min_heap) > n:
            heapq.heappop(min_heap)
    return [-x for x in min_heap]
"""

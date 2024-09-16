
def heap_queue_largest(nums, n):
    heap = list(nums)
    heapq.heapify(heap)
    for _ in range(len(heap) - n):
        heapq.heappop(heap)
    return heap[::-1]



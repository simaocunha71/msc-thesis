import heapq
def heap_queue_largest(nums, n):
    h = []
    for num in nums:
        heapq.heappush(h, -num)
        if len(h) > n:
            heapq.heappop(h)
    return [-x for x in sorted(h, reverse=True)]
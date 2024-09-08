def heap_queue_largest(nums, n):
    import heapq
    return heapq.nlargest(n, nums)
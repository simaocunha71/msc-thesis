def heap_queue_largest(nums, n):
    import heapq
    largest = heapq.nlargest(n, nums)
    return largest
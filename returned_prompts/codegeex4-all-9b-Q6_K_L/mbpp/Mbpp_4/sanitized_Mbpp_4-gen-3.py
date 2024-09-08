def heap_queue_largest(nums, n):
    import heapq
    largest_nums = heapq.nlargest(n, nums)
    return largest_nums
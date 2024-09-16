def heap_queue_largest(nums,n):
    #heapq.nlargest(n, nums)
    import heapq
    return list(reversed(heapq.nlargest(n, nums)))
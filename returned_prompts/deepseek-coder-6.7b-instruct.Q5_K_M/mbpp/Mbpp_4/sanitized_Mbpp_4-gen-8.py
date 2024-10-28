from heapq import nlargest
def heap_queue_largest(nums, n):
    return sorted(nlargest(n, nums), reverse=True)
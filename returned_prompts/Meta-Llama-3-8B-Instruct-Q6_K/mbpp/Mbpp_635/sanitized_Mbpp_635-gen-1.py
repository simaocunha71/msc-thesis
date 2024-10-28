import heapq
def heap_sort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]
    # return [heapq._heapify_max(nums), heapq._heapreplace_max(nums, i) for i in range(len(nums))]
    # return list(heapq.merge(*[heapq.nsmallest(i, nums) for i in range(len(nums))]))
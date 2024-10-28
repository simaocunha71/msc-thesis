import heapq
def heap_sort(nums):
    return list(heapq.heapify(nums))
    # return [heapq.heappop(nums) for _ in range(len(nums))]
    # return sorted(nums)
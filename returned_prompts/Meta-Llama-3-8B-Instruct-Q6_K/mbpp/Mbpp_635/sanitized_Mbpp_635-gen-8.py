import heapq
def heap_sort(nums):
    heapq.heapify(nums)
    sorted_nums = []
    while nums:
        sorted_nums.append(heapq.heappop(nums))
    return sorted_nums
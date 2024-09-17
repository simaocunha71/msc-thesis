import heapq as hq
def heap_sort(nums):
  hq.heapify(nums)
  return [hq.heappop(nums) for _ in range(len(nums))]
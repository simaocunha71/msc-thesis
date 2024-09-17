import heapq as hq
def heap_sort(nums: list) -> list:
  hq.heapify(nums)
  sorted_nums = [hq.heappop(nums) for _ in range(len(nums))]
  return sorted_nums
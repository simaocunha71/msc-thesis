import heapq as hq
def heap_sort(nums: list) -> list:
  sorted_nums = hq.heapify(nums)
  sorted_nums = [hq.heappop(sorted_nums) for _ in range(len(nums))]
  return sorted_nums
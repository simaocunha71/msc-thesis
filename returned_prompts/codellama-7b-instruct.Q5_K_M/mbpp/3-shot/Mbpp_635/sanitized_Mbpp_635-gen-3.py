import heapq as hq
def heap_sort(nums: list) -> list:
  hq.heapify(nums)
  sorted_nums = []
  while nums:
    sorted_nums.append(hq.heappop(nums))
  return sorted_nums
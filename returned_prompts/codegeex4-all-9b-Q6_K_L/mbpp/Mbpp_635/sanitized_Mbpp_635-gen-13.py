import heapq as hq
def heap_sort(nums: list) -> list:
  sorted_nums = hq.heapify(nums)
  return sorted_nums
import heapq as hq
def heap_sort(nums: list) -> list:
  sorted_nums = hq.nsmallest(len(nums), nums)
  return sorted_nums
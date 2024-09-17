import heapq as hq
def heap_sort(nums: list) -> list:
  return hq.nsmallest(len(nums), nums)
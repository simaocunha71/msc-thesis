
import heapq as hq
def heap_sort(nums: list) -> list:
  hq.heapify(nums)
  nums.sort()
  return nums



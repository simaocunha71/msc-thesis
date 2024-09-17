import heapq as hq
def heap_sort(nums: list) -> list:
  nums_copy = nums[:]
  hq.heapify(nums_copy)
  nums.sort()
  return nums
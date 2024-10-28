import heapq
def heap_sort(nums):
  return list(heapq.heapify(nums))
  return sorted(nums) # Alternative solution
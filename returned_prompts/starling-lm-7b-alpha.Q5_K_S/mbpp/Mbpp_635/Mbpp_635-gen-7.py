
def heap_sort(nums: list):
  heapq.heapify(nums)
  while len(nums) > 1:
    yield heapq.heappop(nums)
  return nums



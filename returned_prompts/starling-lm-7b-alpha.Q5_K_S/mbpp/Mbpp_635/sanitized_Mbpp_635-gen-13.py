def heap_sort(nums: list) -> list:
  hq.heapify(nums)
  for _ in range(len(nums)-1, 0, -1):
    hq.heapreplace(nums, hq.heappop(nums))
  return nums
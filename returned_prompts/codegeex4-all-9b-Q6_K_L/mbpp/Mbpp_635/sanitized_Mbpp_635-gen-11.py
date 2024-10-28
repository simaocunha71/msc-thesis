def heap_sort(nums: list) -> list:
  hq.heapify(nums)
  return [hq.heappop(nums) for _ in range(len(nums))]
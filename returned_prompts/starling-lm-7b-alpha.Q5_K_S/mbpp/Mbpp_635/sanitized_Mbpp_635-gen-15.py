def heap_sort(nums: list):
  n = len(nums)
  for i in range(n//2 - 1, -1, -1):
    hq.heapify(nums, i, reverse=True)
  for i in range(n-1, 0, -1):
    nums[i], nums[0] = nums[0], nums[i]
    hq.heapify(nums, 0, reverse=True)
  return nums
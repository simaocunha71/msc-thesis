
def heap_sort(nums: list) -> list:
  hq.heapify(nums)
  for _ in range(len(nums) - 1):
    nums[0], nums[-1] = nums[-1], nums[0]
    hq.heapify(nums)
  return nums



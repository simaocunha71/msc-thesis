def swap_List(nums: list) -> list:
  nums[0], nums[-1] = nums[-1], nums[0]
  return nums
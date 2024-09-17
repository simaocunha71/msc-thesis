def last(nums: list, ele: int) -> int:
  return nums[nums.index(ele)::-1].index(ele)
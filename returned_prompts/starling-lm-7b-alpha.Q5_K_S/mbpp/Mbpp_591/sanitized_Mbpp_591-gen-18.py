def swap_List(nums: list) -> list:
  return nums[0:len(nums)-1]+[nums[len(nums)-1],nums[0]]
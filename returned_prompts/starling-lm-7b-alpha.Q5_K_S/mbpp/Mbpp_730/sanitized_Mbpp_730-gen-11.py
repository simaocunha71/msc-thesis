def consecutive_duplicates(nums: list) -> list:
  nums_no_duplicates = [num for num in nums if num != nums[0] or num != nums[1]]
  return nums_no_duplicates
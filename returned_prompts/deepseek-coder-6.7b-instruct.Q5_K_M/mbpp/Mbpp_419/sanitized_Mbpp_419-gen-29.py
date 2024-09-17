def round_and_sum(nums):
  rounded_nums = [round(num) for num in nums]
  return sum(rounded_nums) * len(rounded_nums)
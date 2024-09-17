def round_and_sum(nums):
  rounded_nums = [round(num) for num in nums]
  sum_nums = sum(rounded_nums)
  return sum_nums * len(rounded_nums)
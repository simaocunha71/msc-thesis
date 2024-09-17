def round_and_sum(nums: list) -> int:
  rounded_nums = [round(num) for num in nums]
  sum_rounded_nums = sum(rounded_nums)
  return sum_rounded_nums * len(rounded_nums)
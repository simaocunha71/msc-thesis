def round_and_sum(nums: list) -> int:
  rounded_nums = [round(num) for num in nums]
  sum_nums = sum(rounded_nums)
  length_nums = len(rounded_nums)
  return sum_nums * length_nums


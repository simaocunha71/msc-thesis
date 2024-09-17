def round_and_sum(nums: list) -> int:
  sum_of_rounded_nums = sum([round(num) for num in nums])
  return sum_of_rounded_nums
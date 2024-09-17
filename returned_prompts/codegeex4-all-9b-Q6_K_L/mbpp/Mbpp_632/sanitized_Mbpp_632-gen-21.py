def move_zero(nums: list) -> list:
  non_zero_nums = [num for num in nums if num != 0]
  zero_nums = [num for num in nums if num == 0]
  return non_zero_nums + zero_nums
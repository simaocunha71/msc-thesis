def remove_odd(nums: list) -> list:
  new_nums = [num for num in nums if num % 2 == 0]
  return new_nums
def diff_even_odd(nums: list) -> int:
  odd_nums = [num for num in nums if num % 2 != 0]
  even_nums = [num for num in nums if num % 2 == 0]
  if len(odd_nums) == 0 or len(even_nums) == 0:
    return 0
  return odd_nums[0] - even_nums[0]
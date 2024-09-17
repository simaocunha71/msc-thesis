def diff_even_odd(nums: list) -> int:
  even_nums = filter(lambda x: x % 2 == 0, nums)
  odd_nums = filter(lambda x: x % 2 != 0, nums)
  return next(even_nums) - next(odd_nums)
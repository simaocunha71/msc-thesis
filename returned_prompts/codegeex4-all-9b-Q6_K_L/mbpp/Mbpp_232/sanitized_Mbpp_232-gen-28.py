def larg_nnum(nums: list, n: int) -> list:
  largest_nums = sorted(nums)[-n:]
  return largest_nums
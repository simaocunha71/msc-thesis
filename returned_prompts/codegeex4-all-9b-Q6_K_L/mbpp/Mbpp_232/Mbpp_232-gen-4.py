def larg_nnum(nums: list, n: int) -> list:
  largest_nums = sorted(nums, reverse=True)[:n]
  return largest_nums
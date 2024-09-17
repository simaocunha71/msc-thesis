def min_k(nums: list,n: int) -> list:
  min_nums = sorted(nums, key = lambda x: x[1])[:n]
  return min_nums
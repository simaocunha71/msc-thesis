def pair_xor_Sum(nums: list,n: int) -> int:
  return sum([sum(x) for x in combinations(nums, r=2)])
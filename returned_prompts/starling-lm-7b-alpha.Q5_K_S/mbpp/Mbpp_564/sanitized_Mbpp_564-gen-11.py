def count_Pairs(nums: list,n: int) -> int:
  return len(set(nums)) * (len(nums)-1)
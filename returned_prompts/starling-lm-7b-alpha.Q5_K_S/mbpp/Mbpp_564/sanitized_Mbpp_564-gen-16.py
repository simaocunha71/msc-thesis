def count_Pairs(nums:list, n:int) -> int:
  return len(set(nums)) * (len(set(nums)) - 1) // 2
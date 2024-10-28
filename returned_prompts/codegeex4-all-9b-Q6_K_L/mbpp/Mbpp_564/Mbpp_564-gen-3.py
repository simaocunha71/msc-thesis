def count_Pairs(nums: list,n: int) -> int:
  return len(list(set((nums[i], nums[j]) for i in range(n) for j in range(i+1, n))))
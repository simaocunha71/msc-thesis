def count_Pairs(nums, n):
  return sum(1 for i in range(n) for j in range(i+1, n) if nums[i] != nums[j])


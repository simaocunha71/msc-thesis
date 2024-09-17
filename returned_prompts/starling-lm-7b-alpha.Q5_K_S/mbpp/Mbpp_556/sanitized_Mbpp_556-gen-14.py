def find_Odd_Pair(nums:list, n:int) -> int:
  odd_pairs = 0
  for i in range(n):
    for j in range(i+1,n):
      if (nums[i]^nums[j])&1:
        odd_pairs += 1
  return odd_pairs
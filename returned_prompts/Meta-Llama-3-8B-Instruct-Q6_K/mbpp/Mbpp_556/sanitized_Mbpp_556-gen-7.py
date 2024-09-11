def find_Odd_Pair(nums, n):
  count = 0
  for i in range(n):
    for j in range(i+1, n):
      if (nums[i]^nums[j]) % 2 != 0:
        count += 1
  return count
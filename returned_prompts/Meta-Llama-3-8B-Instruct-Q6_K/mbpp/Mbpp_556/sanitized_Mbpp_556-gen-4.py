def find_Odd_Pair(nums, k):
  count = 0
  for i in range(k):
    for j in range(i+1, k):
      if (nums[i]^nums[j]) % 2 != 0:
        count += 1
  return count
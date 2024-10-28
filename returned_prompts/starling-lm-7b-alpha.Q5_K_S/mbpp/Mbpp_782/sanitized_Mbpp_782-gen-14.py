def odd_length_sum(nums:list):
  n = len(nums)
  result = 0
  for i in range(n):
    for j in range(i, n):
      if (j - i + 1) % 2 == 1:
        result += sum(nums[i:j + 1])
  return result
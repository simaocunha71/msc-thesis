def odd_length_sum(nums: list) -> int:
  n = len(nums)
  result = 0
  for i in range(n):
    for j in range(i+1, n+1):
      if (j-i) % 2 == 1:
        result += sum(nums[i:j])
  return result
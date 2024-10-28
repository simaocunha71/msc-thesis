def max_sub_array_sum(nums: list, n: int) -> int:
  max_sum = 0
  for i in range(n):
    sum = 0
    for j in range(i+1, n):
      sum += nums[j]
      if sum > max_sum:
        max_sum = sum
  return max_sum
def max_sub_array_sum(nums: list,n: int) -> int:
  max_sum = float('-inf')
  current_sum = 0
  for i in range(n):
    current_sum += nums[i]
    max_sum = max(max_sum, current_sum)
    for j in range(i+1, len(nums)):
      current_sum += nums[j]
      max_sum = max(max_sum, current_sum)
  return max_sum
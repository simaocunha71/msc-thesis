def max_sub_array_sum(nums: list,n: int) -> list:
  max_sum = float('-inf')
  for i in range(n):
    current_sum = sum(nums[i:i+n])
    max_sum = max(max_sum, current_sum)
  return max_sum
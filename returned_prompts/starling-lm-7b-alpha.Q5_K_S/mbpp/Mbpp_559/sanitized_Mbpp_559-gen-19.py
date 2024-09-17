def max_sub_array_sum(nums: list, k: int) -> int:
  result = 0
  for i in range(len(nums)-k+1):
    result += sum(nums[i:i+k])
  return result